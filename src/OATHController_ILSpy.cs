// MobileSecureIT.Data.OATHController
using System;
using System.Globalization;
using System.Security.Cryptography;

public class OATHController
{
	public static int[] digits12 = new int[9] { 1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000 };

	public static string passcode(string input)
	{
		_ = input.Length;
		string text = input.Substring(5, 1).ToString();
		string text2 = input.Substring(10, 1).ToString();
		string text3 = input.Substring(15, 1).ToString();
		string text4 = input.Substring(20, 1).ToString();
		string text5 = input.Substring(25, 1).ToString();
		string text6 = input.Substring(30, 1).ToString();
		return (text + text2 + text3 + text4 + text5 + text6).ToUpper();
	}

	private static byte[] HexString2Bytes(string hexString)
	{
		if (hexString == null)
		{
			return null;
		}
		int length = hexString.Length;
		if (length % 2 == 1)
		{
			return null;
		}
		int num = length / 2;
		byte[] array = new byte[num - 1 + 1];
		try
		{
			for (int i = 0; i != num; i++)
			{
				array[i] = Convert.ToByte(int.Parse(hexString.Substring(i * 2, 2), NumberStyles.HexNumber));
			}
			return array;
		}
		catch (Exception)
		{
			return array;
		}
	}

	public static string GenerateHOTPPassword(string secret, long iterationNumber, int digits = 6)
	{
		byte[] array = BitConverter.GetBytes(iterationNumber);
		if (BitConverter.IsLittleEndian)
		{
			Array.Resize(ref array, 8);
			Array.Reverse((Array)array);
		}
		else
		{
			Array.Reverse((Array)array);
			Array.Resize(ref array, 8);
			Array.Reverse((Array)array);
		}
		byte[] array2 = new HMACSHA1(HexString2Bytes(secret)).ComputeHash(array);
		int num = array2[19] & 0xF;
		return ((((array2[num] & 0x7F) << 24) | ((array2[num + 1] & 0xFF) << 16) | ((array2[num + 2] & 0xFF) << 8) | (array2[num + 3] & 0xFF)) % digits12[digits]).ToString("D" + digits);
	}
}
