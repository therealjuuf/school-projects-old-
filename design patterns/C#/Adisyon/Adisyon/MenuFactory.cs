using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Adisyon
{
	public class _MenuFactory
	{
		public static List<Tatli> Tatlilar = new List<Tatli>();
		public static List<Yemek> Yemekler = new List<Yemek>();
		public static List<Icecek> Icecekler = new List<Icecek>();
		public static MenuElements create_menu(Int32 _ElementID, string _ElementType, string _ElementIsmi, double _Porsiyon, double _Fiyat)
		{
			
			switch (_ElementType)
			{
				case "Tatli":
					
					//Tatlilar.Add(tatil);
					return new Tatli() { ElementID = _ElementID, ElementType = _ElementType, ElementIsmi = _ElementIsmi, Porsiyon = _Porsiyon, Fiyat = _Fiyat };
				case "Yemek":
					return new Yemek() { ElementID = _ElementID, ElementType = _ElementType, ElementIsmi = _ElementIsmi, Porsiyon = _Porsiyon, Fiyat = _Fiyat };
				case "Icecek":
					return new Icecek() { ElementID = _ElementID, ElementType = _ElementType, ElementIsmi = _ElementIsmi, Porsiyon = _Porsiyon, Fiyat = _Fiyat };
				default:
					throw new Exception("Secilien tipte ürün menümüzde mevcut değildir.");
			}
		}

		public class Tatli : MenuElements
		{
			public string ElementType { get; set; }
			public string ElementIsmi { get; set; }
			public Tatli()
			{
				AddToList(this);
			}
			public override void AddToList(object x)
			{
				Tatlilar.Add(x as Tatli);
			}
			public string Isim
			{
				get
				{
					return ElementIsmi;
				}
			}
			
		}

		public class Yemek : MenuElements
		{
			public string ElementType { get; set; }
			public string ElementIsmi { get; set; }
			public Yemek()
			{
				AddToList(this);
			}
			public override void AddToList(object x)
			{
				Yemekler.Add(x as Yemek);
			}
			public string Isim
			{
				get
				{
					return ElementIsmi;
				}
			}
		}

		public class Icecek : MenuElements
		{
			public string ElementType { get; set; }
			public string ElementIsmi { get; set; }
			public Icecek()
			{
				AddToList(this);
			}
			public override void AddToList(object x)
			{
				Icecekler.Add(x as Icecek);
			}
			public string Isim
			{
				get
				{
					return ElementIsmi;
				}
			}
		}

	}
}
