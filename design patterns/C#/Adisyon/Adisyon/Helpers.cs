using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Adisyon
{

	class Helpers
	{
		T[] InitializeArray<T>(int length) where T : new()
		{
			T[] array = new T[length];
			for (int i = 0; i < length; ++i)
			{
				array[i] = new T();
			}

			return array;
		}
	}
}
