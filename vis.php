<?php
if(strtolower(substr(PHP_OS, 0, 3)) == 'win') {
        $R  = "";$RR = "";$G  = "";$GG = "";$C  = "";$CC = "";
        $B  = "";$BB = "";$Y  = "";$YY = "";$P  = "";$X  = "";
} else {
        $R  = "\e[91m";$RR = "\e[91;7m";$G  = "\e[92m";$GG = "\e[92;7m";
        $C  = "\e[36m";$CC = "\e[36;7m";$B  = "\e[94m";$BB = "\e[94;7m";
        $Y  = "\e[93m";$YY = "\e[93;7m";$P  = "\e[35m";$X  = "\e[0m";
        system('clear');
}

$url ="https://clixgenie.com/?ref=yxsgbStVb";
//$url = "https://pds-manggopoh.blogspot.com/";
//$url = 'https://goraps.com/fullpage.php?section=General&pub=454164&ga=g';
$jumlah = "1000000";
$i=1;
$sukses[] = '';
$gagal[] = '';


include "bot.php";
while($i<=$jumlah){
	$userA = explode("\n",file_get_contents("useragent.txt"));
	$uagent = $userA[array_rand($userA)];

$getproxy = explode("\n",file_get_contents("proxy.txt"));
  	$rand = rand(0,20);$proxies = $getproxy[$rand];
	$ambil = explode(':',$proxies);$ip = $ambil[0];$port = $ambil[1];
	//$proxy = $ip.":".$port;
	//$proxy = '192.252.215.5:4145';
$proxy = $getproxy[array_rand($getproxy)];

$_ = view($url,$uagent,$proxy);
  if($_['code']==200){
    echo ketik($G.$i.$P." Status ");echo $G.$_['code'].$Y."	||";echo ketik($C." Sukses	");echo $Y."||".$G." Untuk ";echo ketik("$proxy \n");    $sukses[] = "true";}
else{
    echo ketik($G.$i.$P." Status ");echo $R.$_['code'].$Y." 	||";echo ketik($R." Error	");echo $Y."||".$G." Untuk ";echo ketik($proxy."\n");    $gagal[] = "false";  }
	$i++;	}

	$o = count($sukses)-1;
	$p = count($gagal)-1;
echo $Y."\n[$G Done$Y ] \n";
echo $C."|url =>$B $target \n";
echo $C."|Jumlah Terkirim =>$G $o \n";
echo $C."|Gagal Terkirim =>$R $p \n";

function view($url,$uagent,$proxy){
	$ch = curl_init();
	curl_setopt($ch, CURLOPT_URL, $url);
	curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
	curl_setopt($ch, CURLOPT_PROXYTYPE, CURLPROXY_SOCKS5);
	curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'GET');
	curl_setopt($ch, CURLOPT_PROXY, $proxy);
//	curl_setopt($ch, CURLOPT_HTTPPROXYTUNNEL, 1);
 	curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
	curl_setopt($ch, CURLOPT_TIMEOUT, 0);
$headers = array (
'User-Agent:'.$uagent,
'referer:https://google.com',
'accept-encoding:gzip, deflate, br',
'accept-language:id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,es;q=0.6'
        );
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers); 
$outp = curl_exec($ch);
 $data = curl_getinfo($ch);
 	curl_close($ch);
 	$d['code'] = $data['http_code'];
 	$d['o'] = $outp;
 return $d;
}

?>
