using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using static Adisyon._MenuFactory;
using static Adisyon._Initializer;
using Dapper;

namespace Adisyon
{
	public partial class Form1 : Form
	{
		//T[] InitializeArray<T>(int length) where T : new()
		//{
		//	T[] array = new T[length];
		//	for (int i = 0; i < length; i++)
		//	{
		//		array[i] = new T();
		//	}

		//	return array;
		//}


		public Form1()
		{
			InitializeComponent();
			
		}

		private void Form1_Load(object sender, EventArgs e)
		{

			//create_menu(1, "Tatli", "Baklava", 1.0, 50.2);
			//listBox1.DataSource = Tatlilar;


			
			for(int i = 0; i<10; i++)
			{
				Masalar[i].MasaID = i+1;
			}
		

			using(IDbConnection connection = new System.Data.SqlClient.SqlConnection(Database.ConnectionVal("MSSQLDB")))
			{

				//create_menu(2, "Tatli", "xxx", 1.0, 220.2);
				//var outpa=connection.Query<Tatli>($"select * from Proje.dbo.Menu").ToList();
				//var outpa = connection.Query<Tatli>("exec [dbo].[usp_Read_Tatlilar]").ToList();

				//var outpa = connection.Query<Tatli>("exec [dbo].[usp_Read_Tatlilar]").ToList();

				Yemekler = connection.Query<Yemek>("exec [dbo].[usp_Read_Yemekler]").ToList();
				Tatlilar = connection.Query<Tatli>("exec [dbo].[usp_Read_Tatlilar]").ToList();
				Icecekler = connection.Query<Icecek>("exec [dbo].[usp_Read_Icecekler]").ToList();

				Logs.Items.Insert(0, DateTime.UtcNow + ": Menü güncellendi.");


				var AktifAdisyonlar = connection.Query<DatabaseReader.AktifAdisyon>("exec [dbo].[usp_Read_AktifAdisyon]").ToList();
				//Tatlilar = outpa as List<Tatli>;

				foreach (DatabaseReader.AktifAdisyon element in AktifAdisyonlar)
				{
					Masalar[element.MasaID-1].AdisyonAC();
					Masalar[element.MasaID-1].mAdisyon.Hesap = element.Hesap;
					Masalar[element.MasaID - 1].State = "Dolu";
				}

				Logs.Items.Insert(0, DateTime.UtcNow + ": Aktif adisyonlar güncellendi.");

				var AktifSiparisler = connection.Query<DatabaseReader.ReadAktifSiparis>("exec [dbo].[usp_Read_AktifSiparis]").ToList();
				foreach(DatabaseReader.ReadAktifSiparis element in AktifSiparisler)
				{
					if(element.YemekTipi=="Tatli") Masalar[element.MasaID - 1].mAdisyon.TatliSiparisEkle(element.ElementID, element.Porsiyon,element.Durum);
					else if (element.YemekTipi=="Icecek") Masalar[element.MasaID - 1].mAdisyon.IcecekSiparisEkle(element.ElementID, element.Porsiyon, element.Durum);
					else if (element.YemekTipi=="Yemek") Masalar[element.MasaID - 1].mAdisyon.YemekSiparisEkle(element.ElementID, element.Porsiyon, element.Durum);
				}
				Logs.Items.Insert(0, DateTime.UtcNow + ": Aktif siparişler güncellendi.");

				var Kazanclar = connection.Query<DatabaseReader.Kazanclar>("exec [dbo].[usp_Read_Kazanclar]").ToList();
				foreach(DatabaseReader.Kazanclar element in Kazanclar)
				{
					gunluk.Text = "Günlük Kazanç: " + element.Gunluk.ToString() + " TL";
					haftalik.Text = "Haftalık Kazanç: " + element.Haftalik.ToString() + " TL";
					aylik.Text = "Aylık Kazanç: " + element.Aylik.ToString() + " TL";
				}
				

				//foreach (Tatli element in outpa){
				//	create_menu(element.ElementID, element.ElementType, element.ElementIsmi, element.Porsiyon, element.Fiyat);
				//}

			}
			//for(int i=1; i<21; i++)
			//{
			//	create_menu(i, "Tatli", "Tatli - "+i, 1.0, i*2.30);
			//}
			listBox2.DataSource = Tatlilar;
			listBox2.DisplayMember = "Isim";
			listBox1.DataSource = Yemekler;
			listBox1.DisplayMember = "Isim";
			listBox3.DataSource = Icecekler;
			listBox3.DisplayMember = "Isim";

			//listBox2.Refresh();
			//Masalar[0].AdisyonAC = new Adisyonx();
			//Masalar[0].mAdisyon.TatliSiparisEkle(1, 3);
			//for (int i = 1; i < 21; i++)
			//{
			//	Masalar[0].mAdisyon.TatliSiparisEkle(1, i);
			//}
			////Masalar[0].mAdisyon.TatliSiparisEkle(2, 1);
			//listBox1.DataSource = Masalar[0].mAdisyon.TatliSiparisleri;
			//listBox1.DisplayMember = "Isim";

			//EmptyMasa.DataSource = Masalar.Where((item, index) => Masalar[index].State == "Boş").ToList();
			//EmptyMasa.DisplayMember = "BosMasa";

			//DoluMasa.DataSource = Masalar.Where((item, index) => Masalar[index].State == "Dolu").ToList();
			//DoluMasa.DisplayMember = "DoluMasa";

			RefreshMasaListboxes();
			//var lista = Masalar.Where((item, index) => Masalar[index].mAdisyon.TatliSiparisleri != null).ToList();
			//AktifSiparis.Items.AddRange(lista.Select(x => x.mAdisyon.TatliSiparisleri[0].Fiyat.ToString()).ToArray());
			//foreach (Masa element in Masalar)
			//{
			//	if (element.mAdisyon != null)
			//	{
			//		if(element.mAdisyon.YemekSiparisleri != null)
			//		{
			//			foreach (YemekSiparis x in element.mAdisyon.YemekSiparisleri)
			//			{
			//				//var tatli = (Tatlilar.Where((item, index) => Tatlilar[index].ElementID == x.ElementID));
			//				var tatli = Yemekler.Find(fx => fx.ElementID == x.ElementID);

			//				YemekSiparis.Items.Add("Masa " +element.MasaID +" - "+ x.Porsiyon+" Porisyon "+tatli.ElementIsmi +" Durum: "+ x.Durum);
			//				//AktifSiparis.Items.Add(x.ElementID + " ---- " + x.Durum);
			//				//AktifSiparis.Items.Add(x.ElementID + " ---- " +x.Durum);
			//			}

			//		}
			//	}
			//}

			RefreshYemekSiparis();
			RefreshTatliSiparis();
			RefreshIcecekSiparis();
			Logs.Items.Insert(0, DateTime.UtcNow + ": Masalar güncellendi.");
			
			tabControl1.Selecting += new TabControlCancelEventHandler(tabControl1_Selecting);
			tabPage5.Hide();
			tabControl1.TabPages.Remove(tabPage5);

			YemekSecim.Items.Add("Yemek");
			YemekSecim.Items.Add("Tatlı");
			YemekSecim.Items.Add("İçecek");
		}


		private void RefreshMasaListboxes()
		{
			EmptyMasa.DataSource = Masalar.Where((item, index) => Masalar[index].State == "Boş").ToList();
			EmptyMasa.DisplayMember = "BosMasa";

			DoluMasa.DataSource = Masalar.Where((item, index) => Masalar[index].State == "Dolu").ToList();
			DoluMasa.DisplayMember = "DoluMasa";

			 Logs.Items.Insert(0, DateTime.UtcNow + ": Masalar güncellendi.");
		}

		private void RefreshYemekSiparis()
		{
			YemekSiparis.Items.Clear();
			foreach (Masa element in Masalar)
			{
				if (element.mAdisyon != null)
				{
					if (element.mAdisyon.YemekSiparisleri != null)
					{
						foreach (YemekSiparis x in element.mAdisyon.YemekSiparisleri)
						{
							if (x.Durum == "İletildi")
							{
								//var tatli = (Tatlilar.Where((item, index) => Tatlilar[index].ElementID == x.ElementID));
								var tatli = Yemekler.Find(fx => fx.ElementID == x.ElementID);

								YemekSiparis.Items.Add("Masa " + element.MasaID + " - " + x.Porsiyon + " Porisyon " + tatli.ElementIsmi + " Durum: " + x.Durum);
			
							}
						}

					}
				}
			}
			foreach (Masa element in Masalar)
			{
				if (element.mAdisyon != null)
				{
					if (element.mAdisyon.YemekSiparisleri != null)
					{
						foreach (YemekSiparis x in element.mAdisyon.YemekSiparisleri)
						{
							if (x.Durum == "Hazır")
							{
								//var tatli = (Tatlilar.Where((item, index) => Tatlilar[index].ElementID == x.ElementID));
								var tatli = Yemekler.Find(fx => fx.ElementID == x.ElementID);

								YemekSiparis.Items.Add("Masa " + element.MasaID + " - " + x.Porsiyon + " Porisyon " + tatli.ElementIsmi + " Durum: " + x.Durum);
				
							}
						}

					}
				}
			}
			 Logs.Items.Insert(0, DateTime.UtcNow + ": Yemek listesi güncellendi.");
		}

		private void RefreshTatliSiparis()
		{
			//List<TatliSiparis> tato = new List<TatliSiparis>();
			TatliSiparis.Items.Clear();
			foreach (Masa element in Masalar)
			{
				if (element.mAdisyon != null)
				{
					if (element.mAdisyon.TatliSiparisleri != null)
					{
						foreach (TatliSiparis x in element.mAdisyon.TatliSiparisleri)
						{

							if (x.Durum == "İletildi")
							{
								//var tatli = (Tatlilar.Where((item, index) => Tatlilar[index].ElementID == x.ElementID));
								var tatli = Tatlilar.Find(fx => fx.ElementID == x.ElementID);

								TatliSiparis.Items.Add("Masa " + element.MasaID + " - " + x.Porsiyon + " Porisyon " + tatli.ElementIsmi + " Durum: " + x.Durum);
				
							}
						}

					}
				}
			}
			foreach (Masa element in Masalar)
			{
				if (element.mAdisyon != null)
				{
					if (element.mAdisyon.TatliSiparisleri != null)
					{
						foreach (TatliSiparis x in element.mAdisyon.TatliSiparisleri)
						{

							if (x.Durum == "Hazır")
							{
								//var tatli = (Tatlilar.Where((item, index) => Tatlilar[index].ElementID == x.ElementID));
								var tatli = Tatlilar.Find(fx => fx.ElementID == x.ElementID);

								TatliSiparis.Items.Add("Masa " + element.MasaID + " - " + x.Porsiyon + " Porsiyon " + tatli.ElementIsmi + " Durum: " + x.Durum);
								
							}
						}

					}
				}
			}
			 Logs.Items.Insert(0, DateTime.UtcNow + ": Tatlı listesi güncellendi.");
		}

		private void RefreshIcecekSiparis()
		{
			IcecekSiparis.Items.Clear();
			foreach (Masa element in Masalar)
			{
				if (element.mAdisyon != null)
				{
					if (element.mAdisyon.IcecekSiparisleri != null)
					{
						foreach (IcecekSiparis x in element.mAdisyon.IcecekSiparisleri)
						{
							if (x.Durum == "İletildi")
							{
								//var tatli = (Tatlilar.Where((item, index) => Tatlilar[index].ElementID == x.ElementID));
								var tatli = Icecekler.Find(fx => fx.ElementID == x.ElementID);

								IcecekSiparis.Items.Add("Masa " + element.MasaID + " - " + x.Porsiyon + " Porsiyon " + tatli.ElementIsmi + " Durum: " + x.Durum);
							}
							
						}

					}
				}
			}
			foreach (Masa element in Masalar)
			{
				if (element.mAdisyon != null)
				{
					if (element.mAdisyon.IcecekSiparisleri != null)
					{
						foreach (IcecekSiparis x in element.mAdisyon.IcecekSiparisleri)
						{
							if (x.Durum == "Hazır")
							{
								//var tatli = (Tatlilar.Where((item, index) => Tatlilar[index].ElementID == x.ElementID));
								var tatli = Icecekler.Find(fx => fx.ElementID == x.ElementID);

								IcecekSiparis.Items.Add("Masa " + element.MasaID + " - " + x.Porsiyon + " Porsiyon " + tatli.ElementIsmi + " Durum: " + x.Durum);
							}
							
						}

					}
				}
			}
			 Logs.Items.Insert(0, DateTime.UtcNow + ": İçecek listesi güncellendi.");
		}



		private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
		{
			
		}

		private void listBox2_SelectedIndexChanged(object sender, EventArgs e)
		{

		}

		private void tabControl1_Selecting(object sender, TabControlCancelEventArgs e)
		{

			if (e.TabPage.Name != "tabPage5" && tabControl1.TabPages.Contains(tabPage5))
			{
				comboBox1.Text = "";
				textBox1.Text = "";
				YemekSecim.Text = "";
				tabPage5.Hide();
				tabControl1.TabPages.Remove(tabPage5);
			
			}
			else if(e.TabPage.Name == "tabPage2")
			{
				RefreshMasaListboxes();
			}

			else if (e.TabPage.Name == "tabPage1")
			{
				using (IDbConnection connection = new System.Data.SqlClient.SqlConnection(Database.ConnectionVal("MSSQLDB")))
				{
					var Kazanclar = connection.Query<DatabaseReader.Kazanclar>("exec [dbo].[usp_Read_Kazanclar]").ToList();
					foreach (DatabaseReader.Kazanclar element in Kazanclar)
					{
						gunluk.Text = "Günlük Kazanç: " + element.Gunluk.ToString() + " TL";
						haftalik.Text = "Haftalık Kazanç: " + element.Haftalik.ToString() + " TL";
						aylik.Text = "Aylık Kazanç: " + element.Aylik.ToString() + " TL";
					}
					 Logs.Items.Insert(0, DateTime.UtcNow + ": Günlük kazanç güncellendi.");
				}
			}
			else if(e.TabPage.Name == "tabPage2")
			{
				RefreshYemekSiparis();
				RefreshTatliSiparis();
				RefreshIcecekSiparis();
			}
			
		}

		private void button1_Click(object sender, EventArgs e)
		{
			//listBox2.Update();
			create_menu(5, "Tatli", "Güllaç", 1.0, 30.2);
			
			// listbox display yenileme
			listBox2.DisplayMember = "";
			listBox2.DisplayMember = "Isim";

		}

		private void CreateAdisyon_Click(object sender, EventArgs e)
		{
			if (EmptyMasa.SelectedItem != null)
			{

				Masa SelectedMasa = EmptyMasa.SelectedItem as Masa;
			

				//Masalar[Masalar[EmptyMasa.SelectedIndex].MasaID].AdisyonAC = new Adisyonx();
				using (IDbConnection connection = new System.Data.SqlClient.SqlConnection(Database.ConnectionVal("MSSQLDB")))
				{
					var proc = "[dbo].[usp_Create_Adisyon]";
					var values = new { MasaID = SelectedMasa.MasaID };
					var result = connection.Query(proc, values, commandType: CommandType.StoredProcedure).ToList();
					Masalar[SelectedMasa.MasaID - 1].AdisyonAC();
				}

				Logs.Items.Insert(0, DateTime.UtcNow + ": Masa "+SelectedMasa.MasaID.ToString()+ " için adisyon oluşturuldu.");
				RefreshMasaListboxes();
			}
		}



		private void CloseAdisyon_Click(object sender, EventArgs e)
		{
			if(DoluMasa.SelectedItem != null)
			{
				Masa SelectedMasa = DoluMasa.SelectedItem as Masa;
				

				using (IDbConnection connection = new System.Data.SqlClient.SqlConnection(Database.ConnectionVal("MSSQLDB")))
				{
					var proc = "[dbo].[usp_End_Adisyon]";
					var values = new { MasaID = SelectedMasa.MasaID };
					var result = connection.Query(proc, values, commandType: CommandType.StoredProcedure).ToList();
					Masalar[SelectedMasa.MasaID - 1].AdisyonKapa();
				}
				Logs.Items.Insert(0, DateTime.UtcNow + ": Masa " + SelectedMasa.MasaID.ToString() + " için adisyon kapatıldı.");
				RefreshMasaListboxes();
			}
			
		}

		private void MasaIslemYap_Click(object sender, EventArgs e)
		{
			if (DoluMasa.SelectedItem != null)
			{
				Masa SelectedMasa = DoluMasa.SelectedItem as Masa;
				//TabPage tabPage1 = new TabPage();
				////tabPage1.Name = "Masa" + SelectedMasa.MasaID.ToString() + "Tab";
				//tabPage1.Name = SelectedMasa.MasaID.ToString();
				//tabPage1.Text = "Masa" + SelectedMasa.MasaID.ToString();
				////tabPage1.BackColor = Color.Green;
				////tabPage1.ForeColor = Color.White;
				//tabPage1.Font = new Font("Verdana", 12);
				//tabPage1.Width = 100;
				//tabPage1.Height = 100;
				//tabControl1.TabPages.Add(tabPage1);


				//Button button1 = new Button();
				//button1.Name = "Masa" + SelectedMasa.MasaID.ToString() + "Button";
				//button1.Text = "Masa" + SelectedMasa.MasaID.ToString();
				////button1.BackColor = Color.Blue;
				////button1.ForeColor = Color.White;
				////button1.Font = new Font("Verdana", 12);
				////button1.Width = 100;
				////button1.Height = 30;
				//button1.Location = new Point(200, 200);

				//// Add Button control to TabPage  
				//tabPage1.Controls.Add(button1);
				//button1.Click += new EventHandler(closeTab);

				tabControl1.TabPages.Insert(4, tabPage5);
				tabPage5.Text = "Masa " + SelectedMasa.MasaID.ToString();
				tabPage5.Show();
				tabControl1.SelectedTab = tabPage5;
				Logs.Items.Insert(0, DateTime.UtcNow + ": Masa " + SelectedMasa.MasaID.ToString() + " için işlem yapıldı.");
				MasaHesap.Text = "Hesap : " + Masalar[SelectedMasa.MasaID - 1].mAdisyon.Hesap.ToString() + " TL";

				MasaSiparisGuncelle(SelectedMasa.MasaID);


			}
			//tabControl1.TabPages.Remove(tabPage5);

			



		}

		private void closeTab(object sender, EventArgs e)
		{
			tabControl1.TabPages.Remove(tabControl1.SelectedTab);
		}

		private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
		{

		}

		private void YemekSecim_SelectedIndexChanged(object sender, EventArgs e)
		{
			if (YemekSecim.SelectedIndex == 0)
			{
				//MessageBox.Show(YemekSecim.SelectedText);
				comboBox1.Text = "";
				comboBox1.DataSource = Yemekler;
				comboBox1.DisplayMember = "Isim";
			}
			else if (YemekSecim.SelectedIndex == 1)
			{
				//MessageBox.Show(YemekSecim.SelectedText);
				comboBox1.Text = "";
				comboBox1.DataSource = Tatlilar;
				comboBox1.DisplayMember = "Isim";
			}
			else if (YemekSecim.SelectedIndex == 2)
			{
				//MessageBox.Show(YemekSecim.SelectedText);
				comboBox1.Text = "";
				comboBox1.DataSource = Icecekler;
				comboBox1.DisplayMember = "Isim";
			}
			//MessageBox.Show(YemekSecim.SelectedIndex.ToString());
		}

		private void button2_Click(object sender, EventArgs e)
		{
			tabControl1.TabPages.Insert(4, tabPage5);
			tabPage5.Show();
		}

		private void siparis_ekle_Click(object sender, EventArgs e)
		{
			int index = DoluMasa.SelectedIndex;
			if (DoluMasa.SelectedItem != null && comboBox1.SelectedItem!=null)
			{
				Masa SelectedMasa = DoluMasa.SelectedItem as Masa;

				if (YemekSecim.SelectedIndex == 0)
				{
					
					Yemek Secim = comboBox1.SelectedItem as Yemek;
					SelectedMasa.mAdisyon.YemekSiparisEkle(Secim.ElementID, Convert.ToDouble(textBox1.Text),"İletildi");
					double porsiyon = Convert.ToDouble(textBox1.Text);
					Logs.Items.Insert(0, DateTime.UtcNow + ": Masa " + SelectedMasa.MasaID.ToString() + " siparişlerine "+ porsiyon.ToString() +" porsiyon "+Secim.ElementIsmi+" eklendi.");

					RefreshYemekSiparis();
					RefreshMasaListboxes();
				
					using (IDbConnection connection = new System.Data.SqlClient.SqlConnection(Database.ConnectionVal("MSSQLDB")))
					{
						var proc = "[dbo].[usp_Insert_AktifSiparis]";
						var values = new { MasaID = SelectedMasa.MasaID, ElementID=Secim.ElementID, Porsiyon=porsiyon };
						var result = connection.Query(proc, values, commandType: CommandType.StoredProcedure).ToList();
					}
				}
				else if (YemekSecim.SelectedIndex == 1)
				{
					Tatli Secim = comboBox1.SelectedItem as Tatli;
					SelectedMasa.mAdisyon.TatliSiparisEkle(Secim.ElementID, Convert.ToDouble(textBox1.Text), "İletildi");
					double porsiyon = Convert.ToDouble(textBox1.Text);
					Logs.Items.Insert(0, DateTime.UtcNow + ": Masa " + SelectedMasa.MasaID.ToString() + " siparişlerine " + porsiyon.ToString() + " porsiyon " + Secim.ElementIsmi + " eklendi.");
					RefreshTatliSiparis();
					RefreshMasaListboxes();
					using (IDbConnection connection = new System.Data.SqlClient.SqlConnection(Database.ConnectionVal("MSSQLDB")))
					{
						var proc = "[dbo].[usp_Insert_AktifSiparis]";
						var values = new { MasaID = SelectedMasa.MasaID, ElementID = Secim.ElementID, Porsiyon = porsiyon };
						var result = connection.Query(proc, values, commandType: CommandType.StoredProcedure).ToList();
					}
				}
				else if (YemekSecim.SelectedIndex == 2)
				{
					Icecek Secim = comboBox1.SelectedItem as Icecek;
					SelectedMasa.mAdisyon.IcecekSiparisEkle(Secim.ElementID, Convert.ToDouble(textBox1.Text), "İletildi");
					double porsiyon = Convert.ToDouble(textBox1.Text);
					Logs.Items.Insert(0, DateTime.UtcNow + ": Masa " + SelectedMasa.MasaID.ToString() + " siparişlerine " + porsiyon.ToString() + " porsiyon " + Secim.ElementIsmi + " eklendi.");
					RefreshIcecekSiparis();
					RefreshMasaListboxes();
					using (IDbConnection connection = new System.Data.SqlClient.SqlConnection(Database.ConnectionVal("MSSQLDB")))
					{
						var proc = "[dbo].[usp_Insert_AktifSiparis]";
						var values = new { MasaID = SelectedMasa.MasaID, ElementID = Secim.ElementID, Porsiyon = porsiyon };
						var result = connection.Query(proc, values, commandType: CommandType.StoredProcedure).ToList();
					}
				}
				DoluMasa.SelectedIndex = index;
				MasaSiparisGuncelle(SelectedMasa.MasaID);
				MasaHesap.Text = "Hesap : " + Masalar[SelectedMasa.MasaID - 1].mAdisyon.Hesap.ToString()+" TL";

			}
		}

		private void textBox1_TextChanged(object sender, EventArgs e)
		{

		}

		private void YemekHazir_Click(object sender, EventArgs e)
		{
			if(YemekSiparis.SelectedItem != null)
			{
				string[] words = YemekSiparis.SelectedItem.ToString().Split();
				//MessageBox.Show(words[1]);
				int Masa = Convert.ToInt32(words[1]);
				int Porsiyon = Convert.ToInt32(words[3]);
				string ElementIsmi = words[5];
				int i = 6;
				while (words[i] != "Durum:" || i>15)
				{
					ElementIsmi += " " + words[i];
					i++;
				}
				
				
				if (Masalar[Masa-1].mAdisyon.YemekSiparisleri != null && i<15)
				{
					foreach (YemekSiparis x in Masalar[Masa - 1].mAdisyon.YemekSiparisleri)
					{
						if(x.Porsiyon == Porsiyon)
						{
							var Yemek = Yemekler.Find(fx => fx.ElementID == x.ElementID);
							if (Yemek.ElementIsmi == ElementIsmi)
							{
								Logs.Items.Insert(0, DateTime.UtcNow + ": Masa " + Masa.ToString() + " siparişi hazırlandı.");
								x.Durum = "Hazır";
								RefreshYemekSiparis();
								using (IDbConnection connection = new System.Data.SqlClient.SqlConnection(Database.ConnectionVal("MSSQLDB")))
								{
									var proc = "[dbo].[usp_Update_AktifSiparis]";
									var values = new { MasaID = Masa, ElementID = Yemek.ElementID, Porsiyon = x.Porsiyon };
									var result = connection.Query(proc, values, commandType: CommandType.StoredProcedure).ToList();
								}
							}
						}
						

					}

				}
			}
		}


		private void TatliHazir_Click_1(object sender, EventArgs e)
		{
			if (TatliSiparis.SelectedItem != null)
			{
				string[] words = TatliSiparis.SelectedItem.ToString().Split();
				//MessageBox.Show(words[1]);
				int Masa = Convert.ToInt32(words[1]);
				int Porsiyon = Convert.ToInt32(words[3]);
				string ElementIsmi = words[5];
				//MessageBox.Show(words[3]);
				int i = 6;
				while (words[i] != "Durum:")
				{
					ElementIsmi += " " + words[i];
					i++;
				}
				if (Masalar[Masa - 1].mAdisyon.TatliSiparisleri != null && i < 15)
				{
					foreach (TatliSiparis x in Masalar[Masa - 1].mAdisyon.TatliSiparisleri)
					{
						if (x.Porsiyon == Porsiyon)
						{
							var Yemek = Tatlilar.Find(fx => fx.ElementID == x.ElementID);
							if (Yemek.ElementIsmi == ElementIsmi)
							{
								Logs.Items.Insert(0, DateTime.UtcNow + ": Masa " + Masa.ToString() + " siparişi hazırlandı.");
								x.Durum = "Hazır";
								RefreshTatliSiparis();
								using (IDbConnection connection = new System.Data.SqlClient.SqlConnection(Database.ConnectionVal("MSSQLDB")))
								{
									var proc = "[dbo].[usp_Update_AktifSiparis]";
									var values = new { MasaID = Masa, ElementID = Yemek.ElementID, Porsiyon = x.Porsiyon };
									var result = connection.Query(proc, values, commandType: CommandType.StoredProcedure).ToList();
								}
							}
						}


					}

				}
			}
		}


		private void IcecekHazir_Click(object sender, EventArgs e)
		{
			if (IcecekSiparis.SelectedItem != null)
			{
				string[] words = IcecekSiparis.SelectedItem.ToString().Split();
				//MessageBox.Show(words[1]);
				int Masa = Convert.ToInt32(words[1]);
				int Porsiyon = Convert.ToInt32(words[3]);
				string ElementIsmi = words[5];
				int i = 6;
				while (words[i] != "Durum:" || i > 15)
				{
					ElementIsmi += " " + words[i];
					i++;
				}

				//MessageBox.Show(words[3] + " " + words[5]);

				if (Masalar[Masa - 1].mAdisyon.IcecekSiparisleri != null && i < 15)
				{
					foreach (IcecekSiparis x in Masalar[Masa - 1].mAdisyon.IcecekSiparisleri)
					{
						if (x.Porsiyon == Porsiyon)
						{
							var Yemek = Icecekler.Find(fx => fx.ElementID == x.ElementID);
							if (Yemek.ElementIsmi == ElementIsmi)
							{
								Logs.Items.Insert(0, DateTime.UtcNow + ": Masa " + Masa.ToString() + " siparişi hazırlandı.");
								x.Durum = "Hazır";
								RefreshIcecekSiparis();
								using (IDbConnection connection = new System.Data.SqlClient.SqlConnection(Database.ConnectionVal("MSSQLDB")))
								{
									var proc = "[dbo].[usp_Update_AktifSiparis]";
									var values = new { MasaID = Masa, ElementID = Yemek.ElementID, Porsiyon = x.Porsiyon };
									var result = connection.Query(proc, values, commandType: CommandType.StoredProcedure).ToList();
								}
							}
						}


					}

				}
			}
		}

		private void label7_Click(object sender, EventArgs e)
		{

		}

		private void label10_Click(object sender, EventArgs e)
		{

		}


		public void MasaSiparisGuncelle(int MasaID)
		{
			MasaYemek.Items.Clear();
			MasaTatli.Items.Clear();
			MasaIcecek.Items.Clear();
			if (Masalar[MasaID - 1].mAdisyon.TatliSiparisleri != null)
			{
				foreach (YemekSiparis x in Masalar[MasaID - 1].mAdisyon.YemekSiparisleri)
				{
					var tatli = Yemekler.Find(fx => fx.ElementID == x.ElementID);

					MasaYemek.Items.Add("Masa " + Masalar[MasaID - 1].MasaID + " - " + x.Porsiyon + " Porisyon " + tatli.ElementIsmi + " Durum: " + x.Durum);

				}

			}
			if (Masalar[MasaID - 1].mAdisyon.TatliSiparisleri != null)
			{
				foreach (TatliSiparis x in Masalar[MasaID - 1].mAdisyon.TatliSiparisleri)
				{
					var tatli = Tatlilar.Find(fx => fx.ElementID == x.ElementID);

					MasaTatli.Items.Add("Masa " + Masalar[MasaID - 1].MasaID + " - " + x.Porsiyon + " Porisyon " + tatli.ElementIsmi + " Durum: " + x.Durum);

				}

			}
			if (Masalar[MasaID - 1].mAdisyon.TatliSiparisleri != null)
			{
				foreach (IcecekSiparis x in Masalar[MasaID - 1].mAdisyon.IcecekSiparisleri)
				{
					var tatli = Icecekler.Find(fx => fx.ElementID == x.ElementID);

					MasaIcecek.Items.Add("Masa " + Masalar[MasaID - 1].MasaID + " - " + x.Porsiyon + " Porisyon " + tatli.ElementIsmi + " Durum: " + x.Durum);

				}

			}
		}

		//private void IcecekHazir_Click(object sender, EventArgs e)
		//{

		//}

		//private void TatliHazir_Click_1(object sender, EventArgs e)
		//{

		//}
	}
}
