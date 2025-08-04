using System.Drawing;
using System.Windows.Forms;
using System.Net;
namespace Wanna_Decrypt0r_vN5._0
{
    partial class MainForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        // Declare controls as fields
        private PictureBox picLock;
        private Label lblHeader;
        private ComboBox cmbLanguage;
        private TextBox txtInfo;
        private Panel pnlPayment;
        private Label lblPayment;
        private Label lblTimer1;
        private Panel pnlLoss;
        private Label lblLoss;
        private Label lblTimer2;
        private Panel pnlBitcoin;
        private Button btnCheckPayment;
        private Button btnDecrypt;
        private LinkLabel linkAbout;
        private LinkLabel linkContact;
        private Label lblLossCurrentTime;
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

        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(MainForm));
            this.lblHeader = new System.Windows.Forms.Label();
            this.cmbLanguage = new System.Windows.Forms.ComboBox();
            this.picLock = new System.Windows.Forms.PictureBox();
            this.txtInfo = new System.Windows.Forms.TextBox();
            this.pnlPayment = new System.Windows.Forms.Panel();
            this.linkLabel3 = new System.Windows.Forms.LinkLabel();
            this.lblPayment = new System.Windows.Forms.Label();
            this.lblTimer1 = new System.Windows.Forms.Label();
            this.pnlLoss = new System.Windows.Forms.Panel();
            this.linkLabel2 = new System.Windows.Forms.LinkLabel();
            this.lblLossCurrentTime = new System.Windows.Forms.Label();
            this.lblLoss = new System.Windows.Forms.Label();
            this.lblTimer2 = new System.Windows.Forms.Label();
            this.pnlBitcoin = new System.Windows.Forms.Panel();
            this.picBitcoinLogo = new System.Windows.Forms.PictureBox();
            this.lblBitcoin = new System.Windows.Forms.Label();
            this.txtBitcoin = new System.Windows.Forms.TextBox();
            this.btnCopyBitcoin = new System.Windows.Forms.Button();
            this.lblDecryptKey = new System.Windows.Forms.Label();
            this.txtDecryptKey = new System.Windows.Forms.TextBox();
            this.btnCheckPayment = new System.Windows.Forms.Button();
            this.btnDecrypt = new System.Windows.Forms.Button();
            this.linkAbout = new System.Windows.Forms.LinkLabel();
            this.linkContact = new System.Windows.Forms.LinkLabel();
            this.linkLabel1 = new System.Windows.Forms.LinkLabel();
            ((System.ComponentModel.ISupportInitialize)(this.picLock)).BeginInit();
            this.pnlPayment.SuspendLayout();
            this.pnlLoss.SuspendLayout();
            this.pnlBitcoin.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.picBitcoinLogo)).BeginInit();
            this.SuspendLayout();
            // 
            // lblHeader
            // 
            this.lblHeader.BackColor = System.Drawing.Color.Maroon;
            this.lblHeader.Dock = System.Windows.Forms.DockStyle.Top;
            this.lblHeader.Font = new System.Drawing.Font("Segoe UI", 16F, System.Drawing.FontStyle.Bold);
            this.lblHeader.ForeColor = System.Drawing.Color.White;
            this.lblHeader.Location = new System.Drawing.Point(0, 0);
            this.lblHeader.Name = "lblHeader";
            this.lblHeader.Size = new System.Drawing.Size(1040, 36);
            this.lblHeader.TabIndex = 0;
            this.lblHeader.Text = "Ooops, your files have been encrypted!";
            this.lblHeader.TextAlign = System.Drawing.ContentAlignment.BottomCenter;
            // 
            // cmbLanguage
            // 
            this.cmbLanguage.Items.AddRange(new object[] {
            "English",
            "Vietnamese"});
            this.cmbLanguage.Location = new System.Drawing.Point(916, 12);
            this.cmbLanguage.Name = "cmbLanguage";
            this.cmbLanguage.Size = new System.Drawing.Size(103, 24);
            this.cmbLanguage.TabIndex = 1;
            this.cmbLanguage.Text = "English";
            // 
            // picLock
            // 
            this.picLock.BackColor = System.Drawing.Color.White;
            this.picLock.Location = new System.Drawing.Point(62, 46);
            this.picLock.Name = "picLock";
            this.picLock.Size = new System.Drawing.Size(176, 107);
            this.picLock.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.picLock.TabIndex = 2;
            this.picLock.TabStop = false;
            // 
            // txtInfo
            // 
            this.txtInfo.BackColor = System.Drawing.Color.White;
            this.txtInfo.Font = new System.Drawing.Font("Segoe UI", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.txtInfo.ForeColor = System.Drawing.Color.Black;
            this.txtInfo.Location = new System.Drawing.Point(279, 46);
            this.txtInfo.Multiline = true;
            this.txtInfo.Name = "txtInfo";
            this.txtInfo.ReadOnly = true;
            this.txtInfo.Size = new System.Drawing.Size(750, 372);
            this.txtInfo.TabIndex = 3;
            this.txtInfo.Text = resources.GetString("txtInfo.Text");
            // 
            // pnlPayment
            // 
            this.pnlPayment.BackColor = System.Drawing.Color.DarkRed;
            this.pnlPayment.Controls.Add(this.linkLabel3);
            this.pnlPayment.Controls.Add(this.lblPayment);
            this.pnlPayment.Controls.Add(this.lblTimer1);
            this.pnlPayment.Location = new System.Drawing.Point(17, 159);
            this.pnlPayment.Name = "pnlPayment";
            this.pnlPayment.Size = new System.Drawing.Size(250, 106);
            this.pnlPayment.TabIndex = 4;
            // 
            // linkLabel3
            // 
            this.linkLabel3.AutoSize = true;
            this.linkLabel3.Font = new System.Drawing.Font("Microsoft Sans Serif", 10.2F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.linkLabel3.LinkColor = System.Drawing.SystemColors.Window;
            this.linkLabel3.Location = new System.Drawing.Point(82, 36);
            this.linkLabel3.Name = "linkLabel3";
            this.linkLabel3.Size = new System.Drawing.Size(101, 20);
            this.linkLabel3.TabIndex = 13;
            this.linkLabel3.TabStop = true;
            this.linkLabel3.Text = "Time Left: ";
            // 
            // lblPayment
            // 
            this.lblPayment.AutoSize = true;
            this.lblPayment.Font = new System.Drawing.Font("Segoe UI", 10.8F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblPayment.ForeColor = System.Drawing.Color.Yellow;
            this.lblPayment.Location = new System.Drawing.Point(17, 2);
            this.lblPayment.Name = "lblPayment";
            this.lblPayment.Size = new System.Drawing.Size(230, 25);
            this.lblPayment.TabIndex = 0;
            this.lblPayment.Text = "Payment will be raised on";
            // 
            // lblTimer1
            // 
            this.lblTimer1.AutoSize = true;
            this.lblTimer1.Font = new System.Drawing.Font("Consolas", 18F, System.Drawing.FontStyle.Bold);
            this.lblTimer1.ForeColor = System.Drawing.Color.White;
            this.lblTimer1.Location = new System.Drawing.Point(30, 61);
            this.lblTimer1.Name = "lblTimer1";
            this.lblTimer1.Size = new System.Drawing.Size(191, 36);
            this.lblTimer1.TabIndex = 1;
            this.lblTimer1.Text = "02:23:57:37";
            // 
            // pnlLoss
            // 
            this.pnlLoss.BackColor = System.Drawing.Color.DarkRed;
            this.pnlLoss.Controls.Add(this.linkLabel2);
            this.pnlLoss.Controls.Add(this.lblLossCurrentTime);
            this.pnlLoss.Controls.Add(this.lblLoss);
            this.pnlLoss.Controls.Add(this.lblTimer2);
            this.pnlLoss.Location = new System.Drawing.Point(17, 271);
            this.pnlLoss.Name = "pnlLoss";
            this.pnlLoss.Size = new System.Drawing.Size(250, 147);
            this.pnlLoss.TabIndex = 5;
            // 
            // linkLabel2
            // 
            this.linkLabel2.AutoSize = true;
            this.linkLabel2.Font = new System.Drawing.Font("Microsoft Sans Serif", 10.2F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.linkLabel2.LinkColor = System.Drawing.SystemColors.Window;
            this.linkLabel2.Location = new System.Drawing.Point(77, 69);
            this.linkLabel2.Name = "linkLabel2";
            this.linkLabel2.Size = new System.Drawing.Size(101, 20);
            this.linkLabel2.TabIndex = 12;
            this.linkLabel2.TabStop = true;
            this.linkLabel2.Text = "Time Left: ";
            // 
            // lblLossCurrentTime
            // 
            this.lblLossCurrentTime.AutoSize = true;
            this.lblLossCurrentTime.Font = new System.Drawing.Font("Segoe UI", 10.2F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblLossCurrentTime.ForeColor = System.Drawing.Color.White;
            this.lblLossCurrentTime.Location = new System.Drawing.Point(15, 38);
            this.lblLossCurrentTime.Name = "lblLossCurrentTime";
            this.lblLossCurrentTime.Size = new System.Drawing.Size(151, 23);
            this.lblLossCurrentTime.TabIndex = 5;
            this.lblLossCurrentTime.Text = "Current: 00:00:00";
            // 
            // lblLoss
            // 
            this.lblLoss.AutoSize = true;
            this.lblLoss.Font = new System.Drawing.Font("Segoe UI", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblLoss.ForeColor = System.Drawing.Color.Yellow;
            this.lblLoss.Location = new System.Drawing.Point(7, 3);
            this.lblLoss.Name = "lblLoss";
            this.lblLoss.Size = new System.Drawing.Size(240, 28);
            this.lblLoss.TabIndex = 0;
            this.lblLoss.Text = "Your files will be lost on";
            // 
            // lblTimer2
            // 
            this.lblTimer2.AutoSize = true;
            this.lblTimer2.Font = new System.Drawing.Font("Consolas", 18F, System.Drawing.FontStyle.Bold);
            this.lblTimer2.ForeColor = System.Drawing.Color.White;
            this.lblTimer2.Location = new System.Drawing.Point(30, 98);
            this.lblTimer2.Name = "lblTimer2";
            this.lblTimer2.Size = new System.Drawing.Size(191, 36);
            this.lblTimer2.TabIndex = 1;
            this.lblTimer2.Text = "06:23:57:37";
            // 
            // pnlBitcoin
            // 
            this.pnlBitcoin.BackColor = System.Drawing.Color.DarkRed;
            this.pnlBitcoin.Controls.Add(this.picBitcoinLogo);
            this.pnlBitcoin.Controls.Add(this.lblBitcoin);
            this.pnlBitcoin.Controls.Add(this.txtBitcoin);
            this.pnlBitcoin.Controls.Add(this.btnCopyBitcoin);
            this.pnlBitcoin.Location = new System.Drawing.Point(279, 424);
            this.pnlBitcoin.Name = "pnlBitcoin";
            this.pnlBitcoin.Size = new System.Drawing.Size(753, 116);
            this.pnlBitcoin.TabIndex = 6;
            // 
            // picBitcoinLogo
            // 
            this.picBitcoinLogo.Image = ((System.Drawing.Image)(resources.GetObject("picBitcoinLogo.Image")));
            this.picBitcoinLogo.Location = new System.Drawing.Point(3, 3);
            this.picBitcoinLogo.Name = "picBitcoinLogo";
            this.picBitcoinLogo.Size = new System.Drawing.Size(216, 110);
            this.picBitcoinLogo.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.picBitcoinLogo.TabIndex = 11;
            this.picBitcoinLogo.TabStop = false;
            // 
            // lblBitcoin
            // 
            this.lblBitcoin.Font = new System.Drawing.Font("Segoe UI", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblBitcoin.ForeColor = System.Drawing.Color.Yellow;
            this.lblBitcoin.Location = new System.Drawing.Point(235, 12);
            this.lblBitcoin.Name = "lblBitcoin";
            this.lblBitcoin.Size = new System.Drawing.Size(426, 29);
            this.lblBitcoin.TabIndex = 9;
            this.lblBitcoin.Text = "Send $300 worth of crypto to this address:";
            // 
            // txtBitcoin
            // 
            this.txtBitcoin.BackColor = System.Drawing.Color.DarkRed;
            this.txtBitcoin.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.txtBitcoin.ForeColor = System.Drawing.SystemColors.Window;
            this.txtBitcoin.Location = new System.Drawing.Point(234, 64);
            this.txtBitcoin.Multiline = true;
            this.txtBitcoin.Name = "txtBitcoin";
            this.txtBitcoin.ReadOnly = true;
            this.txtBitcoin.Size = new System.Drawing.Size(427, 38);
            this.txtBitcoin.TabIndex = 10;
            this.txtBitcoin.Text = "22521124$22520471$22520444$22520442";
            // 
            // btnCopyBitcoin
            // 
            this.btnCopyBitcoin.BackColor = System.Drawing.Color.White;
            this.btnCopyBitcoin.Location = new System.Drawing.Point(667, 63);
            this.btnCopyBitcoin.Name = "btnCopyBitcoin";
            this.btnCopyBitcoin.Size = new System.Drawing.Size(73, 39);
            this.btnCopyBitcoin.TabIndex = 12;
            this.btnCopyBitcoin.Text = "Copy";
            this.btnCopyBitcoin.UseVisualStyleBackColor = false;
            this.btnCopyBitcoin.Click += new System.EventHandler(this.btnCopyBitcoin_Click);
            // 
            // lblDecryptKey
            // 
            this.lblDecryptKey.AutoSize = true;
            this.lblDecryptKey.Font = new System.Drawing.Font("Segoe UI", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblDecryptKey.ForeColor = System.Drawing.Color.White;
            this.lblDecryptKey.Location = new System.Drawing.Point(634, 584);
            this.lblDecryptKey.Name = "lblDecryptKey";
            this.lblDecryptKey.Size = new System.Drawing.Size(52, 28);
            this.lblDecryptKey.TabIndex = 5;
            this.lblDecryptKey.Text = "Key:";
            // 
            // txtDecryptKey
            // 
            this.txtDecryptKey.Location = new System.Drawing.Point(686, 583);
            this.txtDecryptKey.Multiline = true;
            this.txtDecryptKey.Name = "txtDecryptKey";
            this.txtDecryptKey.Size = new System.Drawing.Size(346, 30);
            this.txtDecryptKey.TabIndex = 6;
            // 
            // btnCheckPayment
            // 
            this.btnCheckPayment.BackColor = System.Drawing.Color.White;
            this.btnCheckPayment.Cursor = System.Windows.Forms.Cursors.Hand;
            this.btnCheckPayment.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnCheckPayment.Location = new System.Drawing.Point(279, 544);
            this.btnCheckPayment.Name = "btnCheckPayment";
            this.btnCheckPayment.Size = new System.Drawing.Size(352, 32);
            this.btnCheckPayment.TabIndex = 7;
            this.btnCheckPayment.Text = "Check Payment";
            this.btnCheckPayment.UseVisualStyleBackColor = false;
            this.btnCheckPayment.Click += new System.EventHandler(this.btnCheckPayment_Click);
            // 
            // btnDecrypt
            // 
            this.btnDecrypt.BackColor = System.Drawing.Color.White;
            this.btnDecrypt.Cursor = System.Windows.Forms.Cursors.Hand;
            this.btnDecrypt.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnDecrypt.Location = new System.Drawing.Point(686, 544);
            this.btnDecrypt.Name = "btnDecrypt";
            this.btnDecrypt.Size = new System.Drawing.Size(346, 32);
            this.btnDecrypt.TabIndex = 8;
            this.btnDecrypt.Text = "Decrypt";
            this.btnDecrypt.UseVisualStyleBackColor = false;
            this.btnDecrypt.Click += new System.EventHandler(this.btnDecrypt_Click);
            // 
            // linkAbout
            // 
            this.linkAbout.AutoSize = true;
            this.linkAbout.Font = new System.Drawing.Font("Microsoft Sans Serif", 10.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.linkAbout.LinkColor = System.Drawing.Color.Cyan;
            this.linkAbout.Location = new System.Drawing.Point(17, 495);
            this.linkAbout.Name = "linkAbout";
            this.linkAbout.Size = new System.Drawing.Size(221, 20);
            this.linkAbout.TabIndex = 9;
            this.linkAbout.TabStop = true;
            this.linkAbout.Text = "How to buy Cryptocurrency?";
            // 
            // linkContact
            // 
            this.linkContact.AutoSize = true;
            this.linkContact.Font = new System.Drawing.Font("Microsoft Sans Serif", 10.2F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.linkContact.LinkColor = System.Drawing.Color.Cyan;
            this.linkContact.Location = new System.Drawing.Point(17, 556);
            this.linkContact.Name = "linkContact";
            this.linkContact.Size = new System.Drawing.Size(103, 20);
            this.linkContact.TabIndex = 10;
            this.linkContact.TabStop = true;
            this.linkContact.Text = "Contact Us";
            // 
            // linkLabel1
            // 
            this.linkLabel1.AutoSize = true;
            this.linkLabel1.Font = new System.Drawing.Font("Microsoft Sans Serif", 10.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.linkLabel1.LinkColor = System.Drawing.Color.Cyan;
            this.linkLabel1.Location = new System.Drawing.Point(17, 436);
            this.linkLabel1.Name = "linkLabel1";
            this.linkLabel1.Size = new System.Drawing.Size(171, 20);
            this.linkLabel1.TabIndex = 11;
            this.linkLabel1.TabStop = true;
            this.linkLabel1.Text = "About Cryptocurrency";
            // 
            // MainForm
            // 
            this.AutoSize = true;
            this.BackColor = System.Drawing.Color.Maroon;
            this.ClientSize = new System.Drawing.Size(1040, 627);
            this.Controls.Add(this.picLock);
            this.Controls.Add(this.cmbLanguage);
            this.Controls.Add(this.linkLabel1);
            this.Controls.Add(this.lblHeader);
            this.Controls.Add(this.lblDecryptKey);
            this.Controls.Add(this.txtInfo);
            this.Controls.Add(this.pnlPayment);
            this.Controls.Add(this.txtDecryptKey);
            this.Controls.Add(this.pnlLoss);
            this.Controls.Add(this.pnlBitcoin);
            this.Controls.Add(this.btnCheckPayment);
            this.Controls.Add(this.btnDecrypt);
            this.Controls.Add(this.linkAbout);
            this.Controls.Add(this.linkContact);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.MaximizeBox = false;
            this.Name = "MainForm";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Wana Decrypt0r 2.0";
            ((System.ComponentModel.ISupportInitialize)(this.picLock)).EndInit();
            this.pnlPayment.ResumeLayout(false);
            this.pnlPayment.PerformLayout();
            this.pnlLoss.ResumeLayout(false);
            this.pnlLoss.PerformLayout();
            this.pnlBitcoin.ResumeLayout(false);
            this.pnlBitcoin.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.picBitcoinLogo)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private LinkLabel linkLabel1;
        private TextBox txtDecryptKey;
        private Label lblDecryptKey;
        private PictureBox picBitcoinLogo;
        private Label lblBitcoin;
        private TextBox txtBitcoin;
        private Button btnCopyBitcoin;
        private LinkLabel linkLabel3;
        private LinkLabel linkLabel2;
    }
}