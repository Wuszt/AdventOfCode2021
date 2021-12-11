using System;
using System.Collections.Generic;

namespace AOC_10
{
    class Program
    {
        static readonly Dictionary<char, char> s_openToCloseDictionary = new Dictionary<char, char>() { { '(', ')' }, { '{', '}' }, { '<', '>' }, { '[', ']' } };
        static readonly Dictionary<char, UInt32> part1CharToPointsDictionary = new Dictionary<char, UInt32>() { { ')', 3u }, { ']', 57u }, { '}', 1197u }, { '>', 25137u } };
        static readonly Dictionary<char, UInt32> part2CharToPointsDictionary = new Dictionary<char, UInt32>() { { ')', 1u }, { ']', 2u }, { '}', 3u }, { '>', 4u } };


        static void Main(string[] args)
        {
            var fileEnumerator = System.IO.File.ReadLines("../../input.txt");

            UInt32 part1Score = 0u;
            List<UInt64> part2Scores = new List<UInt64>();
            Stack<char> stack = new Stack<char>();
            foreach (var line in fileEnumerator)
            {
                bool incorrect = false;
                stack.Clear();
                foreach (char c in line)
                {
                    if (s_openToCloseDictionary.ContainsKey(c))
                    {
                        stack.Push(s_openToCloseDictionary[c]);
                    }
                    else if (stack.Pop() != c)
                    {
                        incorrect = true;
                        part1Score += part1CharToPointsDictionary[c];
                        break;
                    }
                }

                if (!incorrect && stack.Count > 0)
                {
                    UInt64 sum = 0;
                    foreach( var c in stack )
                    {
                        sum = sum * 5u + (UInt64)part2CharToPointsDictionary[c];
                    }

                    part2Scores.Add(sum);
                }
            }

            Console.WriteLine( "Part1: " + part1Score);

            part2Scores.Sort();
            Console.WriteLine( "Part2: " + part2Scores[ part2Scores.Count / 2 ]);
            Console.ReadKey();
        }
    }
}
