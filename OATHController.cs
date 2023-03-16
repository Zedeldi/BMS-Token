// OATHController is sourced from:
// uk.co.bmsnotts.mobilesecureit.apk > assemblies > MobileSecureIT.dll

// BMSToken provides an interface to OATHController.

using System;
using System.Globalization;
using System.Security.Cryptography;

namespace MobileSecureIT.Data {
    // Token: 0x0200001C RID: 28
    public class OATHController {
        // Token: 0x06000071 RID: 113 RVA: 0x000066D4 File Offset: 0x000048D4
        public static string passcode(string input) {
            int length = input.Length;
            string text = input.Substring(5, 1).ToString();
            string text2 = input.Substring(10, 1).ToString();
            string text3 = input.Substring(15, 1).ToString();
            string text4 = input.Substring(20, 1).ToString();
            string text5 = input.Substring(25, 1).ToString();
            string text6 = input.Substring(30, 1).ToString();
            return string.Concat(new string[] {
                text,
                text2,
                text3,
                text4,
                text5,
                text6
            }).ToUpper();
        }

        // Token: 0x06000072 RID: 114 RVA: 0x00006770 File Offset: 0x00004970
        private static byte[] HexString2Bytes(string hexString) {
            if (hexString == null) {
                return null;
            }
            int length = hexString.Length;
            if (length % 2 == 1) {
                return null;
            }
            int num = length / 2;
            byte[] array = new byte[num - 1 + 1];
            try {
                for (int num2 = 0; num2 != num; num2++) {
                    array[num2] = Convert.ToByte(int.Parse(hexString.Substring(num2 * 2, 2), NumberStyles.HexNumber));
                }
            } catch (Exception) {}
            return array;
        }

        // Token: 0x06000073 RID: 115 RVA: 0x000067E0 File Offset: 0x000049E0
        public static string GenerateHOTPPassword(string secret, long iterationNumber, int digits = 6) {
            byte[] bytes = BitConverter.GetBytes(iterationNumber);
            if (BitConverter.IsLittleEndian) {
                Array.Resize < byte > (ref bytes, 8);
                Array.Reverse(bytes);
            } else {
                Array.Reverse(bytes);
                Array.Resize < byte > (ref bytes, 8);
                Array.Reverse(bytes);
            }
            byte[] array = new HMACSHA1(OATHController.HexString2Bytes(secret)).ComputeHash(bytes);
            int num = (int)(array[19] & 15);
            return (((int)(array[num] & 127) << 24 | (int)(array[num + 1] & byte.MaxValue) << 16 | (int)(array[num + 2] & byte.MaxValue) << 8 | (int)(array[num + 3] & byte.MaxValue)) % OATHController.digits12[digits]).ToString("D" + digits.ToString());
        }

        // Token: 0x0400006E RID: 110
        public static int[] digits12 = new int[] {
            1,
            10,
            100,
            1000,
            10000,
            100000,
            1000000,
            10000000,
            100000000
        };
    }

    public class BMSToken {

        public static void printUsageAndExit() {
            // Print usage message and exit.
            Console.WriteLine(
                "Usage: {0} <gen|verify> <secret> <iteration|passcode>",
                System.AppDomain.CurrentDomain.FriendlyName
            );
            Console.WriteLine("======");
            Console.WriteLine("gen: generate token for secret at index iteration (negative for range)");
            Console.WriteLine("verify: verify passcode for the specified secret");
            System.Environment.Exit(1);
        }

        public static string[] genMany(string secret, long maxIteration) {
            // Generate many HOTP passwords and return array.
            string[] tokens = new string[maxIteration + 1];
            for (int n = 0; n <= maxIteration; n++) {
                tokens[n] = OATHController.GenerateHOTPPassword(secret, n);
            }
            return tokens;
        }

        public static void Main(string[] args) {
            // Main entry point to handle args and output.
            if (args.Length < 3) {
                BMSToken.printUsageAndExit();
            }
            string mode = args[0].ToLower();
            string secret = args[1];
            if (mode == "gen") {
                long iterationNumber = long.Parse(args[2]);
                Console.WriteLine("Secret: {0}", secret);
                // If iterationNumber is negative, generate all tokens in range.
                if (iterationNumber < 0) {
                    string[] tokens = BMSToken.genMany(secret, Math.Abs(iterationNumber));
                    for (int i = 0; i < tokens.Length; i++) {
                        Console.WriteLine("#{0}: {1}", i, tokens[i]);
                    }
                }
                else {
                    string token = OATHController.GenerateHOTPPassword(secret, iterationNumber);
                    Console.WriteLine("#{0}: {1}", iterationNumber, token);
                }
            }
            else if (mode == "verify") {
                string passcode = args[2].ToUpper();
                string expectedPasscode = OATHController.passcode(secret);
                bool match = false;
                if (passcode == expectedPasscode) {
                    match = true;
                }
                Console.WriteLine(
                    "Secret: {0}\nPasscode: {1} (Expected: {2})\nMatch: {3}",
                    secret, passcode, expectedPasscode, match
                );
            }
            else {
                BMSToken.printUsageAndExit();
            }
        }
    }
}
