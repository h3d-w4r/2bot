<?php

$jumlah = "1000000";
$i=1;
$sukses[] = '';
$gagal[] = '';

while($i<=$jumlah){

$uid = '33884';
$nomor = '62813'.rand(0000, 99999).'5'.rand(000, 999);
$body = 'reference_user_id='.$uid.'&username='.$nomor;
$userA = explode("\n",file_get_contents("useragent.txt"));
        $uagent = $userA[array_rand($userA)];

$getproxy = explode("\n",file_get_contents("proxy.txt"));
        $rand = rand(0,20);$proxies = $getproxy[$rand];
$ambil = explode(':',$proxies);$ip = $ambil[0];
$port = $ambil[1];
        //$proxy = $ip.":".$port;
        //$proxy = '192.252.215.5:4145';
$proxy = $getproxy[array_rand($getproxy)];

$_=block($body,$uagent,$proxy);
	if($_['code']==200){
echo "Sukses || nomor =>".$nomor." || ip => ".$proxy."\n";
$sukses[] = "true";}
	else {
echo " Gagal || nomor =>".$nomor." || ip => ".$proxy."\n";
$gagal[] = "false";  } $i++;   }

        $o = count($sukses)-1;
        $p = count($gagal)-1;
echo $Y."\n[$G Done$Y ] \n";
echo $C."|url =>$B $target \n";
echo $C."|Jumlah Terkirim =>$G $o \n";
echo $C."|Gagal Terkirim =>$R $p \n";


function block($body,$uagent,$proxy) {
$url = 'http://apk.getdana.online/index.php';
$ch = curl_init();
 curl_setopt($ch, CURLOPT_URL, $url);
 curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'POST');
 curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS, $body);
// curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
 curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
 curl_setopt($ch, CURLOPT_PROXYTYPE, CURLPROXY_SOCKS5);
 curl_setopt($ch, CURLOPT_PROXY, $proxy);
        curl_setopt($ch, CURLOPT_HTTPPROXYTUNNEL, 1);
        curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
        curl_setopt($ch, CURLOPT_TIMEOUT, 8);
$headers = array (
'User-Agent:'.$uagent,
'Content-Type:application/x-www-form-urlencoded',
'Referer:https://getdana.online/index.php?refer=33884',
'Cookie:PHPSESSID=f08c4af25dea1a9e7232dcd34e86bbf3'.
'X-Requested-With:https.getdana.online',
        );
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
$outp = curl_exec($ch);
 $data = curl_getinfo($ch);
        curl_close($ch);
        $d['code'] = $data['http_code'];
        $d['o'] = $outp;
 return $d;
}
