using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Adisyon
{
	public abstract class MenuElements
	{
		public Int32 ElementID { get; set; }
		public double Porsiyon { get; set; }
		public double Fiyat { get; set; }

		public abstract void AddToList(object x);
	}
}
