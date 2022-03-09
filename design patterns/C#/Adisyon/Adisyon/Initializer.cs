using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static Adisyon._MenuFactory;
using System.Windows.Forms;

namespace Adisyon
{
	public class _Initializer
	{
		static T[] InitializeArray<T>(int length) where T : new()
		{
			T[] array = new T[length];
			for (int i = 0; i < length; i++)
			{
				array[i] = new T();
			}

			return array;
		}

		public static Masa[] Masalar = InitializeArray<Masa>(10);


	}
}
