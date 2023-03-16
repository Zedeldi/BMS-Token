# BMS-Token

[![GitHub last commit](https://img.shields.io/github/last-commit/Zedeldi/BMS-Token?style=flat-square)](https://github.com/Zedeldi/BMS-Token/commits)

BMS/Secure-IT Token OATHController.

## Description

### OATHController

`OATHController.cs` extracted from `uk.co.bmsnotts.mobilesecureit.apk`, which uses the [Xamarin](https://dotnet.microsoft.com/en-us/apps/xamarin) platform, with an added command-line interface.

`dnSpy` was used to decompile `uk.co.bmsnotts.mobilesecureit.apk/assemblies/MobileSecureIT.dll`.

The passcode used to verify the secret is the 5, 10, 15, 20, 25 and 30th character of the secret.

The method for generating HOTP tokens can be found in `OATHController.GenerateHOTPPassword`.

### Database interface

A Python interface to the Secure-IT Token SQLite3 database can be found in `bms.py`.

The database can be found in the following location on Android:

`/data/data/uk.co.bmsnotts.mobilesecureit/files/LocalDB.db3`

## Installation

Compile `OATHController.cs` with Mono:
  - `mcs OATHController.cs`

## Usage

`mono OATHController.exe <gen|verify> <secret> <iteration|passcode>`
- `gen`: generate token for secret at index iteration (negative for range)
- `verify`: verify passcode for the specified secret

## Credits

Secure-IT Token = <https://play.google.com/store/apps/details?id=uk.co.bmsnotts.mobilesecureit>

dnSpy = <https://github.com/dnSpy/dnSpy>
