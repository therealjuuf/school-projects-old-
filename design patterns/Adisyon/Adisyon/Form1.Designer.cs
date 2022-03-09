namespace Adisyon
{
	partial class Form1
	{
		/// <summary>
		/// Required designer variable.
		/// </summary>
		private System.ComponentModel.IContainer components = null;

		/// <summary>
		/// Clean up any resources being used.
		/// </summary>
		/// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
		protected override void Dispose(bool disposing)
		{
			if (disposing && (components != null))
			{
				components.Dispose();
			}
			base.Dispose(disposing);
		}

		#region Windows Form Designer generated code

		/// <summary>
		/// Required method for Designer support - do not modify
		/// the contents of this method with the code editor.
		/// </summary>
		private void InitializeComponent()
		{
			System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
			this.listBox1 = new System.Windows.Forms.ListBox();
			this.listBox2 = new System.Windows.Forms.ListBox();
			this.label1 = new System.Windows.Forms.Label();
			this.label2 = new System.Windows.Forms.Label();
			this.label3 = new System.Windows.Forms.Label();
			this.label4 = new System.Windows.Forms.Label();
			this.tabControl1 = new System.Windows.Forms.TabControl();
			this.tabPage1 = new System.Windows.Forms.TabPage();
			this.aylik = new System.Windows.Forms.Label();
			this.haftalik = new System.Windows.Forms.Label();
			this.gunluk = new System.Windows.Forms.Label();
			this.label7 = new System.Windows.Forms.Label();
			this.listBox3 = new System.Windows.Forms.ListBox();
			this.tabPage2 = new System.Windows.Forms.TabPage();
			this.MasaIslemYap = new System.Windows.Forms.Button();
			this.CloseAdisyon = new System.Windows.Forms.Button();
			this.label6 = new System.Windows.Forms.Label();
			this.DoluMasa = new System.Windows.Forms.ListBox();
			this.CreateAdisyon = new System.Windows.Forms.Button();
			this.label5 = new System.Windows.Forms.Label();
			this.EmptyMasa = new System.Windows.Forms.ListBox();
			this.tabPage3 = new System.Windows.Forms.TabPage();
			this.YemekHazir = new System.Windows.Forms.Button();
			this.IcecekHazir = new System.Windows.Forms.Button();
			this.TatliHazir = new System.Windows.Forms.Button();
			this.IcecekSiparis = new System.Windows.Forms.ListBox();
			this.TatliSiparis = new System.Windows.Forms.ListBox();
			this.YemekSiparis = new System.Windows.Forms.ListBox();
			this.tabPage4 = new System.Windows.Forms.TabPage();
			this.Logs = new System.Windows.Forms.ListBox();
			this.tabPage5 = new System.Windows.Forms.TabPage();
			this.label13 = new System.Windows.Forms.Label();
			this.label12 = new System.Windows.Forms.Label();
			this.label11 = new System.Windows.Forms.Label();
			this.MasaIcecek = new System.Windows.Forms.ListBox();
			this.MasaTatli = new System.Windows.Forms.ListBox();
			this.MasaYemek = new System.Windows.Forms.ListBox();
			this.MasaHesap = new System.Windows.Forms.Label();
			this.label10 = new System.Windows.Forms.Label();
			this.label9 = new System.Windows.Forms.Label();
			this.label8 = new System.Windows.Forms.Label();
			this.textBox1 = new System.Windows.Forms.TextBox();
			this.siparis_ekle = new System.Windows.Forms.Button();
			this.YemekSecim = new System.Windows.Forms.ComboBox();
			this.comboBox1 = new System.Windows.Forms.ComboBox();
			this.tabControl1.SuspendLayout();
			this.tabPage1.SuspendLayout();
			this.tabPage2.SuspendLayout();
			this.tabPage3.SuspendLayout();
			this.tabPage4.SuspendLayout();
			this.tabPage5.SuspendLayout();
			this.SuspendLayout();
			// 
			// listBox1
			// 
			this.listBox1.DisplayMember = "(none)";
			this.listBox1.FormattingEnabled = true;
			this.listBox1.Location = new System.Drawing.Point(192, 41);
			this.listBox1.Name = "listBox1";
			this.listBox1.Size = new System.Drawing.Size(182, 316);
			this.listBox1.TabIndex = 0;
			this.listBox1.SelectedIndexChanged += new System.EventHandler(this.listBox1_SelectedIndexChanged);
			// 
			// listBox2
			// 
			this.listBox2.FormattingEnabled = true;
			this.listBox2.Location = new System.Drawing.Point(6, 41);
			this.listBox2.Name = "listBox2";
			this.listBox2.Size = new System.Drawing.Size(164, 316);
			this.listBox2.TabIndex = 1;
			this.listBox2.SelectedIndexChanged += new System.EventHandler(this.listBox2_SelectedIndexChanged);
			// 
			// label1
			// 
			this.label1.AutoSize = true;
			this.label1.Location = new System.Drawing.Point(0, 0);
			this.label1.Name = "label1";
			this.label1.Size = new System.Drawing.Size(35, 13);
			this.label1.TabIndex = 3;
			this.label1.Text = "label1";
			// 
			// label2
			// 
			this.label2.Location = new System.Drawing.Point(0, 0);
			this.label2.Name = "label2";
			this.label2.Size = new System.Drawing.Size(100, 23);
			this.label2.TabIndex = 0;
			// 
			// label3
			// 
			this.label3.AutoSize = true;
			this.label3.Location = new System.Drawing.Point(189, 23);
			this.label3.Name = "label3";
			this.label3.Size = new System.Drawing.Size(86, 13);
			this.label3.TabIndex = 4;
			this.label3.Text = "Yiyecek Menüsü";
			// 
			// label4
			// 
			this.label4.AutoSize = true;
			this.label4.Location = new System.Drawing.Point(6, 23);
			this.label4.Name = "label4";
			this.label4.Size = new System.Drawing.Size(68, 13);
			this.label4.TabIndex = 5;
			this.label4.Text = "Tatli Menüsü";
			// 
			// tabControl1
			// 
			this.tabControl1.Controls.Add(this.tabPage1);
			this.tabControl1.Controls.Add(this.tabPage2);
			this.tabControl1.Controls.Add(this.tabPage3);
			this.tabControl1.Controls.Add(this.tabPage4);
			this.tabControl1.Controls.Add(this.tabPage5);
			this.tabControl1.Location = new System.Drawing.Point(15, 16);
			this.tabControl1.Name = "tabControl1";
			this.tabControl1.SelectedIndex = 0;
			this.tabControl1.Size = new System.Drawing.Size(773, 422);
			this.tabControl1.TabIndex = 6;
			// 
			// tabPage1
			// 
			this.tabPage1.AllowDrop = true;
			this.tabPage1.Controls.Add(this.aylik);
			this.tabPage1.Controls.Add(this.haftalik);
			this.tabPage1.Controls.Add(this.gunluk);
			this.tabPage1.Controls.Add(this.label7);
			this.tabPage1.Controls.Add(this.listBox3);
			this.tabPage1.Controls.Add(this.listBox2);
			this.tabPage1.Controls.Add(this.label3);
			this.tabPage1.Controls.Add(this.label4);
			this.tabPage1.Controls.Add(this.listBox1);
			this.tabPage1.Location = new System.Drawing.Point(4, 22);
			this.tabPage1.Name = "tabPage1";
			this.tabPage1.Padding = new System.Windows.Forms.Padding(3);
			this.tabPage1.Size = new System.Drawing.Size(765, 396);
			this.tabPage1.TabIndex = 0;
			this.tabPage1.Text = "Ana Ekran";
			this.tabPage1.UseVisualStyleBackColor = true;
			// 
			// aylik
			// 
			this.aylik.AutoSize = true;
			this.aylik.Location = new System.Drawing.Point(603, 150);
			this.aylik.Name = "aylik";
			this.aylik.Size = new System.Drawing.Size(74, 13);
			this.aylik.TabIndex = 10;
			this.aylik.Text = "Aylık Kazanç: ";
			this.aylik.Click += new System.EventHandler(this.label10_Click);
			// 
			// haftalik
			// 
			this.haftalik.AutoSize = true;
			this.haftalik.Location = new System.Drawing.Point(603, 93);
			this.haftalik.Name = "haftalik";
			this.haftalik.Size = new System.Drawing.Size(88, 13);
			this.haftalik.TabIndex = 9;
			this.haftalik.Text = "Haftalık Kazanç: ";
			// 
			// gunluk
			// 
			this.gunluk.AutoSize = true;
			this.gunluk.Location = new System.Drawing.Point(603, 41);
			this.gunluk.Name = "gunluk";
			this.gunluk.Size = new System.Drawing.Size(86, 13);
			this.gunluk.TabIndex = 8;
			this.gunluk.Text = "Günlük Kazanç: ";
			// 
			// label7
			// 
			this.label7.AutoSize = true;
			this.label7.Location = new System.Drawing.Point(392, 25);
			this.label7.Name = "label7";
			this.label7.Size = new System.Drawing.Size(81, 13);
			this.label7.TabIndex = 7;
			this.label7.Text = "İçecek Menüsü";
			this.label7.Click += new System.EventHandler(this.label7_Click);
			// 
			// listBox3
			// 
			this.listBox3.DisplayMember = "(none)";
			this.listBox3.FormattingEnabled = true;
			this.listBox3.Location = new System.Drawing.Point(395, 41);
			this.listBox3.Name = "listBox3";
			this.listBox3.Size = new System.Drawing.Size(182, 316);
			this.listBox3.TabIndex = 6;
			// 
			// tabPage2
			// 
			this.tabPage2.Controls.Add(this.MasaIslemYap);
			this.tabPage2.Controls.Add(this.CloseAdisyon);
			this.tabPage2.Controls.Add(this.label6);
			this.tabPage2.Controls.Add(this.DoluMasa);
			this.tabPage2.Controls.Add(this.CreateAdisyon);
			this.tabPage2.Controls.Add(this.label5);
			this.tabPage2.Controls.Add(this.EmptyMasa);
			this.tabPage2.Location = new System.Drawing.Point(4, 22);
			this.tabPage2.Name = "tabPage2";
			this.tabPage2.Padding = new System.Windows.Forms.Padding(3);
			this.tabPage2.Size = new System.Drawing.Size(765, 396);
			this.tabPage2.TabIndex = 1;
			this.tabPage2.Text = "Masalar";
			this.tabPage2.UseVisualStyleBackColor = true;
			// 
			// MasaIslemYap
			// 
			this.MasaIslemYap.Location = new System.Drawing.Point(614, 207);
			this.MasaIslemYap.Name = "MasaIslemYap";
			this.MasaIslemYap.Size = new System.Drawing.Size(106, 23);
			this.MasaIslemYap.TabIndex = 6;
			this.MasaIslemYap.Text = "İşlem Yap";
			this.MasaIslemYap.UseVisualStyleBackColor = true;
			this.MasaIslemYap.Click += new System.EventHandler(this.MasaIslemYap_Click);
			// 
			// CloseAdisyon
			// 
			this.CloseAdisyon.Location = new System.Drawing.Point(502, 207);
			this.CloseAdisyon.Name = "CloseAdisyon";
			this.CloseAdisyon.Size = new System.Drawing.Size(106, 23);
			this.CloseAdisyon.TabIndex = 5;
			this.CloseAdisyon.Text = "Adisyonu Kapa";
			this.CloseAdisyon.UseVisualStyleBackColor = true;
			this.CloseAdisyon.Click += new System.EventHandler(this.CloseAdisyon_Click);
			// 
			// label6
			// 
			this.label6.AutoSize = true;
			this.label6.Location = new System.Drawing.Point(499, 12);
			this.label6.Name = "label6";
			this.label6.Size = new System.Drawing.Size(69, 13);
			this.label6.TabIndex = 4;
			this.label6.Text = "Dolu Masalar";
			// 
			// DoluMasa
			// 
			this.DoluMasa.FormattingEnabled = true;
			this.DoluMasa.Location = new System.Drawing.Point(502, 28);
			this.DoluMasa.Name = "DoluMasa";
			this.DoluMasa.Size = new System.Drawing.Size(241, 173);
			this.DoluMasa.TabIndex = 3;
			// 
			// CreateAdisyon
			// 
			this.CreateAdisyon.Location = new System.Drawing.Point(31, 207);
			this.CreateAdisyon.Name = "CreateAdisyon";
			this.CreateAdisyon.Size = new System.Drawing.Size(106, 23);
			this.CreateAdisyon.TabIndex = 2;
			this.CreateAdisyon.Text = "Adisyon Aç";
			this.CreateAdisyon.UseVisualStyleBackColor = true;
			this.CreateAdisyon.Click += new System.EventHandler(this.CreateAdisyon_Click);
			// 
			// label5
			// 
			this.label5.AutoSize = true;
			this.label5.Location = new System.Drawing.Point(28, 12);
			this.label5.Name = "label5";
			this.label5.Size = new System.Drawing.Size(65, 13);
			this.label5.TabIndex = 1;
			this.label5.Text = "Boş Masalar";
			// 
			// EmptyMasa
			// 
			this.EmptyMasa.FormattingEnabled = true;
			this.EmptyMasa.Location = new System.Drawing.Point(31, 28);
			this.EmptyMasa.Name = "EmptyMasa";
			this.EmptyMasa.Size = new System.Drawing.Size(241, 173);
			this.EmptyMasa.TabIndex = 0;
			// 
			// tabPage3
			// 
			this.tabPage3.Controls.Add(this.YemekHazir);
			this.tabPage3.Controls.Add(this.IcecekHazir);
			this.tabPage3.Controls.Add(this.TatliHazir);
			this.tabPage3.Controls.Add(this.IcecekSiparis);
			this.tabPage3.Controls.Add(this.TatliSiparis);
			this.tabPage3.Controls.Add(this.YemekSiparis);
			this.tabPage3.Location = new System.Drawing.Point(4, 22);
			this.tabPage3.Name = "tabPage3";
			this.tabPage3.Size = new System.Drawing.Size(765, 396);
			this.tabPage3.TabIndex = 2;
			this.tabPage3.Text = "Siparişler";
			this.tabPage3.UseVisualStyleBackColor = true;
			// 
			// YemekHazir
			// 
			this.YemekHazir.Location = new System.Drawing.Point(86, 370);
			this.YemekHazir.Name = "YemekHazir";
			this.YemekHazir.Size = new System.Drawing.Size(75, 23);
			this.YemekHazir.TabIndex = 6;
			this.YemekHazir.Text = "Hazır";
			this.YemekHazir.UseVisualStyleBackColor = true;
			this.YemekHazir.Click += new System.EventHandler(this.YemekHazir_Click);
			// 
			// IcecekHazir
			// 
			this.IcecekHazir.Location = new System.Drawing.Point(593, 370);
			this.IcecekHazir.Name = "IcecekHazir";
			this.IcecekHazir.Size = new System.Drawing.Size(75, 23);
			this.IcecekHazir.TabIndex = 5;
			this.IcecekHazir.Text = "Hazır";
			this.IcecekHazir.UseVisualStyleBackColor = true;
			this.IcecekHazir.Click += new System.EventHandler(this.IcecekHazir_Click);
			// 
			// TatliHazir
			// 
			this.TatliHazir.Location = new System.Drawing.Point(338, 370);
			this.TatliHazir.Name = "TatliHazir";
			this.TatliHazir.Size = new System.Drawing.Size(75, 23);
			this.TatliHazir.TabIndex = 4;
			this.TatliHazir.Text = "Hazır";
			this.TatliHazir.UseVisualStyleBackColor = true;
			this.TatliHazir.Click += new System.EventHandler(this.TatliHazir_Click_1);
			// 
			// IcecekSiparis
			// 
			this.IcecekSiparis.FormattingEnabled = true;
			this.IcecekSiparis.Location = new System.Drawing.Point(523, 37);
			this.IcecekSiparis.Name = "IcecekSiparis";
			this.IcecekSiparis.Size = new System.Drawing.Size(215, 329);
			this.IcecekSiparis.TabIndex = 3;
			// 
			// TatliSiparis
			// 
			this.TatliSiparis.FormattingEnabled = true;
			this.TatliSiparis.Location = new System.Drawing.Point(273, 37);
			this.TatliSiparis.Name = "TatliSiparis";
			this.TatliSiparis.Size = new System.Drawing.Size(215, 329);
			this.TatliSiparis.TabIndex = 2;
			// 
			// YemekSiparis
			// 
			this.YemekSiparis.FormattingEnabled = true;
			this.YemekSiparis.Location = new System.Drawing.Point(21, 37);
			this.YemekSiparis.Name = "YemekSiparis";
			this.YemekSiparis.Size = new System.Drawing.Size(215, 329);
			this.YemekSiparis.TabIndex = 1;
			// 
			// tabPage4
			// 
			this.tabPage4.Controls.Add(this.Logs);
			this.tabPage4.Location = new System.Drawing.Point(4, 22);
			this.tabPage4.Name = "tabPage4";
			this.tabPage4.Size = new System.Drawing.Size(765, 396);
			this.tabPage4.TabIndex = 3;
			this.tabPage4.Text = "Loglar";
			this.tabPage4.UseVisualStyleBackColor = true;
			// 
			// Logs
			// 
			this.Logs.FormattingEnabled = true;
			this.Logs.Location = new System.Drawing.Point(27, 24);
			this.Logs.Name = "Logs";
			this.Logs.Size = new System.Drawing.Size(702, 342);
			this.Logs.TabIndex = 1;
			// 
			// tabPage5
			// 
			this.tabPage5.Controls.Add(this.label13);
			this.tabPage5.Controls.Add(this.label12);
			this.tabPage5.Controls.Add(this.label11);
			this.tabPage5.Controls.Add(this.MasaIcecek);
			this.tabPage5.Controls.Add(this.MasaTatli);
			this.tabPage5.Controls.Add(this.MasaYemek);
			this.tabPage5.Controls.Add(this.MasaHesap);
			this.tabPage5.Controls.Add(this.label10);
			this.tabPage5.Controls.Add(this.label9);
			this.tabPage5.Controls.Add(this.label8);
			this.tabPage5.Controls.Add(this.textBox1);
			this.tabPage5.Controls.Add(this.siparis_ekle);
			this.tabPage5.Controls.Add(this.YemekSecim);
			this.tabPage5.Controls.Add(this.comboBox1);
			this.tabPage5.Location = new System.Drawing.Point(4, 22);
			this.tabPage5.Name = "tabPage5";
			this.tabPage5.Size = new System.Drawing.Size(765, 396);
			this.tabPage5.TabIndex = 4;
			this.tabPage5.Text = "Masa";
			this.tabPage5.UseVisualStyleBackColor = true;
			// 
			// label13
			// 
			this.label13.AutoSize = true;
			this.label13.Location = new System.Drawing.Point(499, 105);
			this.label13.Name = "label13";
			this.label13.Size = new System.Drawing.Size(87, 13);
			this.label13.TabIndex = 18;
			this.label13.Text = "İçecek Siparişleri";
			// 
			// label12
			// 
			this.label12.AutoSize = true;
			this.label12.Location = new System.Drawing.Point(268, 105);
			this.label12.Name = "label12";
			this.label12.Size = new System.Drawing.Size(74, 13);
			this.label12.TabIndex = 17;
			this.label12.Text = "Tatlı Siparişleri";
			// 
			// label11
			// 
			this.label11.AutoSize = true;
			this.label11.Location = new System.Drawing.Point(37, 105);
			this.label11.Name = "label11";
			this.label11.Size = new System.Drawing.Size(87, 13);
			this.label11.TabIndex = 16;
			this.label11.Text = "Yemek Siparişleri";
			// 
			// MasaIcecek
			// 
			this.MasaIcecek.FormattingEnabled = true;
			this.MasaIcecek.Location = new System.Drawing.Point(502, 121);
			this.MasaIcecek.Name = "MasaIcecek";
			this.MasaIcecek.Size = new System.Drawing.Size(215, 186);
			this.MasaIcecek.TabIndex = 15;
			// 
			// MasaTatli
			// 
			this.MasaTatli.FormattingEnabled = true;
			this.MasaTatli.Location = new System.Drawing.Point(271, 121);
			this.MasaTatli.Name = "MasaTatli";
			this.MasaTatli.Size = new System.Drawing.Size(215, 186);
			this.MasaTatli.TabIndex = 14;
			// 
			// MasaYemek
			// 
			this.MasaYemek.FormattingEnabled = true;
			this.MasaYemek.Location = new System.Drawing.Point(40, 121);
			this.MasaYemek.Name = "MasaYemek";
			this.MasaYemek.Size = new System.Drawing.Size(215, 186);
			this.MasaYemek.TabIndex = 13;
			// 
			// MasaHesap
			// 
			this.MasaHesap.AutoSize = true;
			this.MasaHesap.Location = new System.Drawing.Point(37, 334);
			this.MasaHesap.Name = "MasaHesap";
			this.MasaHesap.Size = new System.Drawing.Size(44, 13);
			this.MasaHesap.TabIndex = 12;
			this.MasaHesap.Text = "Hesap: ";
			// 
			// label10
			// 
			this.label10.AutoSize = true;
			this.label10.Location = new System.Drawing.Point(356, 22);
			this.label10.Name = "label10";
			this.label10.Size = new System.Drawing.Size(81, 13);
			this.label10.TabIndex = 11;
			this.label10.Text = "Porsiyon Miktarı";
			// 
			// label9
			// 
			this.label9.AutoSize = true;
			this.label9.Location = new System.Drawing.Point(202, 22);
			this.label9.Name = "label9";
			this.label9.Size = new System.Drawing.Size(38, 13);
			this.label9.TabIndex = 10;
			this.label9.Text = "Sipariş";
			// 
			// label8
			// 
			this.label8.AutoSize = true;
			this.label8.Location = new System.Drawing.Point(37, 22);
			this.label8.Name = "label8";
			this.label8.Size = new System.Drawing.Size(58, 13);
			this.label8.TabIndex = 9;
			this.label8.Text = "Sipariş Tipi";
			// 
			// textBox1
			// 
			this.textBox1.Location = new System.Drawing.Point(359, 38);
			this.textBox1.Name = "textBox1";
			this.textBox1.Size = new System.Drawing.Size(100, 20);
			this.textBox1.TabIndex = 3;
			this.textBox1.TextChanged += new System.EventHandler(this.textBox1_TextChanged);
			// 
			// siparis_ekle
			// 
			this.siparis_ekle.Location = new System.Drawing.Point(480, 36);
			this.siparis_ekle.Name = "siparis_ekle";
			this.siparis_ekle.Size = new System.Drawing.Size(75, 23);
			this.siparis_ekle.TabIndex = 2;
			this.siparis_ekle.Text = "Ekle";
			this.siparis_ekle.UseVisualStyleBackColor = true;
			this.siparis_ekle.Click += new System.EventHandler(this.siparis_ekle_Click);
			// 
			// YemekSecim
			// 
			this.YemekSecim.FormattingEnabled = true;
			this.YemekSecim.Location = new System.Drawing.Point(40, 38);
			this.YemekSecim.Name = "YemekSecim";
			this.YemekSecim.Size = new System.Drawing.Size(121, 21);
			this.YemekSecim.TabIndex = 1;
			this.YemekSecim.SelectedIndexChanged += new System.EventHandler(this.YemekSecim_SelectedIndexChanged);
			// 
			// comboBox1
			// 
			this.comboBox1.FormattingEnabled = true;
			this.comboBox1.Location = new System.Drawing.Point(205, 38);
			this.comboBox1.Name = "comboBox1";
			this.comboBox1.Size = new System.Drawing.Size(121, 21);
			this.comboBox1.TabIndex = 0;
			this.comboBox1.SelectedIndexChanged += new System.EventHandler(this.comboBox1_SelectedIndexChanged);
			// 
			// Form1
			// 
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.ClientSize = new System.Drawing.Size(800, 450);
			this.Controls.Add(this.tabControl1);
			this.Controls.Add(this.label2);
			this.Controls.Add(this.label1);
			this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
			this.Name = "Form1";
			this.Text = "Adisyonx";
			this.Load += new System.EventHandler(this.Form1_Load);
			this.tabControl1.ResumeLayout(false);
			this.tabPage1.ResumeLayout(false);
			this.tabPage1.PerformLayout();
			this.tabPage2.ResumeLayout(false);
			this.tabPage2.PerformLayout();
			this.tabPage3.ResumeLayout(false);
			this.tabPage4.ResumeLayout(false);
			this.tabPage5.ResumeLayout(false);
			this.tabPage5.PerformLayout();
			this.ResumeLayout(false);
			this.PerformLayout();

		}

		#endregion

		private System.Windows.Forms.ListBox listBox1;
		private System.Windows.Forms.ListBox listBox2;
		private System.Windows.Forms.Label label1;
		private System.Windows.Forms.Label label2;
		private System.Windows.Forms.Label label3;
		private System.Windows.Forms.Label label4;
		private System.Windows.Forms.TabPage tabPage1;
		private System.Windows.Forms.TabPage tabPage2;
		private System.Windows.Forms.TabPage tabPage3;
		private System.Windows.Forms.TabPage tabPage4;
		private System.Windows.Forms.Button CreateAdisyon;
		private System.Windows.Forms.Label label5;
		private System.Windows.Forms.ListBox EmptyMasa;
		private System.Windows.Forms.Label label6;
		private System.Windows.Forms.ListBox DoluMasa;
		private System.Windows.Forms.Button CloseAdisyon;
		private System.Windows.Forms.ListBox YemekSiparis;
		private System.Windows.Forms.Button MasaIslemYap;
		private System.Windows.Forms.ComboBox comboBox1;
		private System.Windows.Forms.ComboBox YemekSecim;
		public System.Windows.Forms.TabPage tabPage5;
		private System.Windows.Forms.TabControl tabControl1;
		private System.Windows.Forms.Button siparis_ekle;
		private System.Windows.Forms.TextBox textBox1;
		private System.Windows.Forms.ListBox IcecekSiparis;
		private System.Windows.Forms.ListBox TatliSiparis;
		private System.Windows.Forms.Button YemekHazir;
		private System.Windows.Forms.Button IcecekHazir;
		private System.Windows.Forms.Button TatliHazir;
		private System.Windows.Forms.Label label7;
		private System.Windows.Forms.ListBox listBox3;
		private System.Windows.Forms.Label aylik;
		private System.Windows.Forms.Label haftalik;
		private System.Windows.Forms.Label gunluk;
		private System.Windows.Forms.ListBox Logs;
		private System.Windows.Forms.Label MasaHesap;
		private System.Windows.Forms.Label label10;
		private System.Windows.Forms.Label label9;
		private System.Windows.Forms.Label label8;
		private System.Windows.Forms.Label label13;
		private System.Windows.Forms.Label label12;
		private System.Windows.Forms.Label label11;
		private System.Windows.Forms.ListBox MasaIcecek;
		private System.Windows.Forms.ListBox MasaTatli;
		private System.Windows.Forms.ListBox MasaYemek;
	}
}

