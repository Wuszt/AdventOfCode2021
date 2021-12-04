#include "../Framework/Framework.h"
#include <immintrin.h>
#include <fstream>
#include <vector>
#include <sstream>
#include <array>
#include <assert.h>

#define BOARD_DIMENSION 5
#define BOARD_SIZE BOARD_DIMENSION * BOARD_DIMENSION

const __m256i c_zero = _mm256_set1_epi32( 0 );

struct Winners
{
	std::vector< int > m_indices;
	std::vector< int > m_scores;

	bool AnyWinner() const
	{
		return !m_indices.empty();
	}
};

struct Boards
{
	std::vector< std::array< int, BOARD_SIZE > > m_boards;
	std::vector< __m256i > m_sums;

	void CreateBoard( std::ifstream& input )
	{
		m_boards.emplace_back();
		m_sums.emplace_back();
		for ( int i = 0; i < BOARD_SIZE; ++i )
		{
			input >> m_boards.back()[ i ];
			m_sums.back().m256i_i32[ i % BOARD_DIMENSION ] += m_boards.back()[ i ];
		}

		m_boards.emplace_back();
		m_sums.emplace_back();
		auto& originalBoard = m_boards[ m_boards.size() - 2u ];
		for ( int x = 0; x < BOARD_DIMENSION; ++x )
		{
			for ( int y = 0; y < BOARD_DIMENSION; ++y )
			{
				int transposedIndex = y * BOARD_DIMENSION + x;
				m_boards.back()[ transposedIndex ] = originalBoard[ x * BOARD_DIMENSION + y ];
				m_sums.back().m256i_i32[ x ] += m_boards.back()[ transposedIndex ];
			}
		}
	}

	void RemoveBoards( std::vector< int >&& indices )
	{
		std::sort( indices.begin(), indices.end() );

		for ( int i = indices.size() - 1; i >= 0; --i )
		{
			int coIndex = indices[ i ] - indices[ i ] % 2;

			std::swap( m_boards[ coIndex ], m_boards.back() );
			std::swap( m_boards[ coIndex + 1 ], m_boards[ m_boards.size() - 2 ] );
			m_boards.pop_back();
			m_boards.pop_back();

			std::swap( m_sums[ coIndex ], m_sums.back() );
			std::swap( m_sums[ coIndex + 1 ], m_sums[ m_sums.size() - 2 ] );
			m_sums.pop_back();
			m_sums.pop_back();
		}
	}

	Winners AreYouWinningSon( int inputNr )
	{
		Winners winners;
		__m256i input = _mm256_set1_epi32( inputNr );

		for ( int b = 0; b < m_boards.size(); b += 2 )
		{
			bool isWinner = false;
			for ( int x = 0; x < 2 && !isWinner; ++x )
			{
				int bucketIndex = b + x;
				for ( int i = 0; i < BOARD_SIZE && !isWinner; i += 5 )
				{
					__m256i row = _mm256_load_si256( ( __m256i* ) &m_boards[ bucketIndex ][ i ] );
					__m256i compare = _mm256_cmpeq_epi32( input, row );
					m_sums[ bucketIndex ] = _mm256_add_epi32( _mm256_mullo_epi32( row, compare ), m_sums[ bucketIndex ] );

					__m256i result = _mm256_cmpeq_epi32( m_sums[ bucketIndex ], c_zero );

					for ( int j = 0; j < BOARD_DIMENSION; ++j )
					{
						if ( result.m256i_i32[ j ] != 0 )
						{
							isWinner = true;
							winners.m_scores.emplace_back();
							for ( int s = 0; s < BOARD_DIMENSION; ++s )
							{
								winners.m_scores.back() += m_sums[ bucketIndex ].m256i_i32[ s ];
							}

							winners.m_indices.emplace_back( bucketIndex );
							break;
						}
					}
				}
			}
		}

		return winners;
	}
};

int main()
{
	std::ifstream file( "input.txt" );
	std::string sInput;
	Boards boards;

	file >> sInput;

	while ( !file.eof() )
	{
		boards.CreateBoard( file );
	}

	std::stringstream ss( sInput );
	int place = 1;
	for ( int inputNr; ss >> inputNr; )
	{
		if ( ss.peek() == ',' )
		{
			ss.ignore();
		}

		Winners winners = boards.AreYouWinningSon( inputNr );
		if ( winners.AnyWinner() )
		{
			std::cout << "New winners: ";
			for ( auto score : winners.m_scores )
			{
				std::cout << score * inputNr << ",";
			}

			std::cout << "\n";

			boards.RemoveBoards( std::move( winners.m_indices ) );
		}
	}
}