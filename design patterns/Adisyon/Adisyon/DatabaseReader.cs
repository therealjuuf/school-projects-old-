using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Adisyon
{
	public static class DatabaseReader
	{
		public class AktifAdisyon
		{
			public Int32 MasaID;
			public Int64 Hesap;
		}

		public class ReadAktifSiparis
		{
			public Int32 MasaID;
			public Int32 ElementID;
			public string YemekTipi;
			public double Porsiyon;
			public string Durum;
		}

		public class Kazanclar
		{
			public double Gunluk;
			public double Haftalik;
			public double Aylik;
		}


	}
}
