#pragma once
#include <iostream>
#include <chrono>

#define SW( name ) auto stopwatch_##name = StopWatch( #name, 1u );
#define SW_IT( name, iterations ) auto stopwatch_##name = StopWatch( #name, iterations );

class StopWatch
{
public:
	StopWatch( const char* name, long iterations )
		: m_name( name )
		, m_iterations( iterations )
	{
		m_start = std::chrono::high_resolution_clock::now();
	}

	~StopWatch()
	{
		auto duration = std::chrono::duration_cast<std::chrono::microseconds>( std::chrono::high_resolution_clock::now() - m_start ).count();

		double result = static_cast< double >( duration ) / static_cast< double >( m_iterations );

		std::cout << m_name << ": " << result << "\n";
	}

private:
	const char* m_name;
	long m_iterations;
	std::chrono::time_point< std::chrono::steady_clock > m_start;
};