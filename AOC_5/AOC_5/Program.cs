using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Numerics;
using System.IO;

namespace AOC_5
{

	struct Line
	{
		public static Dictionary<Vector2, bool> dict = new Dictionary<Vector2, bool>();

		public Line( Vector2 start, Vector2 end )
		{
			m_start = start;
			m_dir = end - start;
			m_length = m_dir.Length();
			m_dir /= m_length;
		}

		private float CrossVectors( Vector2 a, Vector2 b )
		{
			return a.X * b.Y - a.Y * b.X;
		}
		private bool IsSmallerOrAlmostEqual(float a, float b)
		{
			return a < b || Math.Abs(a) - Math.Abs(b) < 0.001f;
		}

		public void ComputeIntersections( Line line )
		{
			float rsCross = CrossVectors(m_dir, line.m_dir);
			float qprCross = CrossVectors(line.m_start - m_start, m_dir);

			float myDenominator = IsHorizontalOrVertical() ? 1.0f : (float)Math.Sqrt(2);
			float otherDenominator = line.IsHorizontalOrVertical() ? 1.0f : (float)Math.Sqrt(2);

			Vector2 roundedDir = new Vector2(Math.Sign( m_dir.X ), Math.Sign( m_dir.Y ));
			if ( rsCross == 0 )
			{
				if ( qprCross == 0.0f )
				{
					Vector2 secondStart = Vector2.Dot(m_dir, line.m_dir) > 0 ? line.m_start : line.m_start + line.m_dir * line.m_length;
					Vector2 startsDiff = secondStart - m_start;
					float dot = Vector2.Dot(startsDiff, m_dir);
					float length = startsDiff.Length();

					Vector2 myStart = dot <= 0.0f ? m_start : secondStart;

					float lf;
					if (dot == 0.0f)
					{
						lf = ( Math.Min(m_length, line.m_length) ) / myDenominator;
					}
					else if (dot > 0)
					{
						lf = Math.Min(m_length - length, line.m_length) / otherDenominator;
					}
					else
					{
						lf = Math.Min(line.m_length - length, m_length ) / myDenominator;
					}

					int l = (int)(lf + 0.5f);
					for (int i = 0; i <= l; ++i)
					{
						dict[myStart + roundedDir * i] = true;
					}
				}
			}
			else
			{
				float u = qprCross / rsCross;
				if( u >= 0.0f && IsSmallerOrAlmostEqual( u, line.m_length ) )
				{
					float qpsCross = CrossVectors(line.m_start - m_start, line.m_dir);
					float t = qpsCross / rsCross;
					if( t >= 0.0f && IsSmallerOrAlmostEqual( t, m_length ) )
					{
						float fT = t / myDenominator;
						float diff = fT - (int)fT;
						if ( Math.Abs(diff - 0.5f) > 0.001f )
						{
							dict[m_start + roundedDir * (int)(t / myDenominator + 0.5f)] = true;
						}
					}
				}
			}
		}

		public bool IsHorizontalOrVertical()
		{
			return Math.Abs(m_dir.X) == 1 || Math.Abs(m_dir.Y) == 1;
		}

		Vector2 m_start;
		Vector2 m_dir;
		float m_length;
	}

	class Program
	{
		static void Main(string[] args)
		{
			var fileEnumerator = System.IO.File.ReadLines("../../input.txt");

			string[] arrow = { " -> " };
			Line[] lines = fileEnumerator.SelectMany(x => x.Split(arrow, StringSplitOptions.None))
				.SelectMany(x => x.Split(','))
				.Select((value, index) => new { value = Int32.Parse(value), index }).GroupBy(g => g.index / 4, x => x.value)
				.Select(x => new Line(new Vector2(x.ElementAt(0), x.ElementAt(1)), new Vector2(x.ElementAt(2), x.ElementAt(3))))
				//.Where(x => x.IsHorizontalOrVertical() ) // comment it for part 2
				.ToArray();

			for (int i = 0; i < lines.Length; ++i)
			{
				for (int j = i + 1; j < lines.Length; ++j)
				{
					lines[i].ComputeIntersections(lines[j]);
				}
			}

			Console.WriteLine( Line.dict.Count );
			Console.ReadKey();
		}
	}
}
