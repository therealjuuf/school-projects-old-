using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static Adisyon._MenuFactory;

namespace Adisyon
{
	
	public class Masa
	{
		public Int32 MasaID;
		public Adisyonx mAdisyon { get; set; }
		public string State = "Boş";


		//public Adisyonx xAdisyonAC
		//{
		//	set
		//	{
		//		this.mAdisyon = new Adisyonx();
		//		Random rnd = new Random();
		//		this.mAdisyon.Hesap = rnd.Next(1, 50);
		//		this.State = "Dolu";

		//	}
		//}

		public void AdisyonAC()
		{
			this.mAdisyon = new Adisyonx();
			//Random rnd = new Random();
			//this.mAdisyon.Hesap = rnd.Next(1, 50);
			this.State = "Dolu";
		}


		public void AdisyonKapa()
		{
				this.State = "Boş";
		}

		public string BosMasa
		{
			get
			{
				return "Masa: "+MasaID.ToString();
			}
		}
		public string DoluMasa
		{
			get
			{
				return "Masa " + MasaID.ToString() +" - Güncel hesap: " + this.mAdisyon.Hesap.ToString()+" TL";
			}
		}

		public string Siparisler
		{
			get
			{
				return "Tatli Siparisi" + " --- Fiyat: " + mAdisyon.TatliSiparisleri[0].Fiyat + " TL " + "Durum: " + mAdisyon.TatliSiparisleri[0].Durum;
			}
		}

	}

	public class Adisyonx
	{
		public List<YemekSiparis> YemekSiparisleri = new List<YemekSiparis>();
		public List<TatliSiparis> TatliSiparisleri = new List<TatliSiparis>();
		public List<IcecekSiparis> IcecekSiparisleri = new List<IcecekSiparis>();
		public double Hesap = 0;


		public void YemekSiparisEkle(Int32 _ElementID, double _PorsiyonSayisi, string _Durum)
		{
			var xMenuElement = _MenuFactory.Yemekler.Find(item => item.ElementID == _ElementID);
			YemekSiparisleri.Add(new YemekSiparis { ElementID = _ElementID, Porsiyon = _PorsiyonSayisi, Fiyat = xMenuElement.Fiyat * _PorsiyonSayisi, Durum = _Durum });
			Hesap += xMenuElement.Fiyat * _PorsiyonSayisi;
		}

		public void TatliSiparisEkle(Int32 _ElementID, double _PorsiyonSayisi, string _Durum)
		{
			var xMenuElement = _MenuFactory.Tatlilar.Find(item => item.ElementID == _ElementID);
			TatliSiparisleri.Add(new TatliSiparis { ElementID = _ElementID, Porsiyon = _PorsiyonSayisi, Fiyat = xMenuElement.Fiyat * _PorsiyonSayisi, Durum= _Durum });
			Hesap += xMenuElement.Fiyat * _PorsiyonSayisi;
		}

		public void IcecekSiparisEkle(Int32 _ElementID, double _PorsiyonSayisi,string _Durum)
		{
			var xMenuElement = _MenuFactory.Icecekler.Find(item => item.ElementID == _ElementID);
			IcecekSiparisleri.Add(new IcecekSiparis { ElementID = _ElementID, Porsiyon = _PorsiyonSayisi, Fiyat = xMenuElement.Fiyat * _PorsiyonSayisi, Durum =  _Durum });
			Hesap += xMenuElement.Fiyat * _PorsiyonSayisi;
		}

	}


	public class TatliSiparis : MenuElements
	{
		public string Durum;

		

		public override void AddToList(object x)
		{
			throw new NotImplementedException();
		}

		public string Isim
		{
			get
			{
				return Tatlilar[ElementID].ElementIsmi + " --- Fiyat: " + Fiyat + " TL --- " + "Durum: " +Durum + "     " + Porsiyon;
			}
		}



	}
	public class YemekSiparis : MenuElements
	{
		public string Durum;

		public override void AddToList(object x)
		{
			throw new NotImplementedException();
		}

		public string Isim
		{
			get
			{
				return Tatlilar[ElementID].ElementIsmi + " --- Fiyat: " + Fiyat + " TL --- " + "Durum: " + Durum + "     " + Porsiyon;
			}
		}
	}

	public class IcecekSiparis : MenuElements
	{
		public string Durum;

		public override void AddToList(object x)
		{
			throw new NotImplementedException();
		}

		public string Isim
		{
			get
			{
				return Tatlilar[ElementID].ElementIsmi + " --- Fiyat: " + Fiyat + " TL --- " + "Durum: " + Durum + "     " + Porsiyon;
			}
		}
	}

}
