#!/bin/sh
security unlock-keychain -p <System Password>  /Users/Admin/Library/Keychains/login.keychain

echo Archiving Scheme
xcodebuild -project <Project Name> -scheme <Scheme Name> archive -archivePath <Path to archive>
xcodebuild -exportArchive -exportFormat ipa -archivePath <Absolute/Path/To/Archive.xcarchive> -exportPath <Absolute/Path/For/IPA.ipa>
