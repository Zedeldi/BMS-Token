# BMS-Token

[![GitHub last commit](https://img.shields.io/github/last-commit/Zedeldi/BMS-Token?style=flat-square)](https://github.com/Zedeldi/BMS-Token/commits)

BMS/Secure-IT Token OATHController.

## Description

### OATHController

`src/OATHController.cs` extracted from `uk.co.bmsnotts.mobilesecureit.apk`, which uses the [Xamarin](https://dotnet.microsoft.com/en-us/apps/xamarin) platform, with an added command-line interface.

`dnSpy` and `ILSpy` were used to decompile `uk.co.bmsnotts.mobilesecureit.apk/assemblies/MobileSecureIT.dll`.

The passcode used to verify the secret is the 5th, 10th, 15th, 20th, 25th and 30th characters of the secret (zero-indexed).

The method for generating HOTP tokens can be found in `OATHController.GenerateHOTPPassword`.

### Database interface

A Python interface to the Secure-IT Token SQLite3 database can be found in `bms_token.db`.

The database can be found in the following location on Android:

`/data/data/uk.co.bmsnotts.mobilesecureit/files/LocalDB.db3`

## Build

To use the C# command-line interface, compile the modified source.

### Compile

Compile `src/OATHController.cs` with Mono:
 
  - `mcs OATHController.cs`

### Usage

`mono OATHController.exe <gen|verify> <secret> <iteration|passcode>`

  - `gen`: generate token for secret at index iteration (negative for range)

  - `verify`: verify passcode for the specified secret


### Python Wrapper

A Python wrapper for the C# classes is found in `bms_token.wrapper`.

Compile `src/OATHController.cs` with Mono as a library:
 
  - `mcs -t:library OATHController.cs`

Then copy the built DLL to `bms_token/wrapper/bin/`.

A command-line interface for the wrapper is also provided:

  - `python -m bms_token`

## Credits

Secure-IT Token = <https://play.google.com/store/apps/details?id=uk.co.bmsnotts.mobilesecureit>

dnSpy = <https://github.com/dnSpy/dnSpy>

ILSpy = <https://github.com/icsharpcode/ILSpy>
