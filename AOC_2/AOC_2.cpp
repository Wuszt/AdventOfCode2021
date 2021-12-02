// AOC_2.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <fstream>
#include <iosfwd>
#include <string>

void Part1()
{
	std::ifstream input( "input.txt" );
	std::string cmd;
	int delta = 0;

	int x = 0;
	int y = 0;

	while( input >> cmd >> delta )
	{
		switch( cmd[ 0 ] )
		{
		case 'f':
			x += delta;
			break;

		case 'd':
			y += delta;
			break;

		case 'u':
			y -= delta;
			break;
		}
	}

	std::cout << x * y << "\n";
}

void Part2()
{
	std::ifstream input( "input.txt" );
	std::string cmd;
	int delta = 0;

	int x = 0;
	int y = 0;
	int aim = 0;

	while( input >> cmd >> delta )
	{
		switch( cmd[ 0 ] )
		{
		case 'f':
			y += delta * aim;
			x += delta;
			break;

		case 'd':
			aim += delta;
			break;

		case 'u':
			aim -= delta;
			break;
		}
	}

	std::cout << x * y << "\n";
}

int main()
{
	Part2();
}