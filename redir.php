<?php
$url = 'http://raboninco.com/1NRNe';
 $ch = curl_init();
 curl_setopt($ch, CURLOPT_URL, $url);
 curl_setopt($ch, CURLOPT_RETURNTRANSFER, TRUE);
 curl_setopt($ch, CURLOPT_FOLLOWLOCATION, TRUE);
 $headers = array (
'user-agent:'.$ua,
'referer:http://bloghedwar.blogspot.com/'
        );
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
$html = curl_exec($ch);
 $urlredir = curl_getinfo($ch, CURLINFO_EFFECTIVE_URL);
echo " redirect to => ".$urlredir."\n";
 curl_close($ch);


function view($urlredir){
$z7 = curl_init();
 curl_setopt($z7, CURLOPT_URL, $urlredir);
 curl_setopt($z7, CURLOPT_REFERER, "https://www.google.com");
 curl_setopt($z7, CURLOPT_HEADER, 0);
 curl_setopt($z7, CURLOPT_FOLLOWLOCATION, true);
 curl_setopt($z7, CURLOPT_RETURNTRANSFER, true);
// curl_setopt($z7, CURLOPT_PROXYTYPE, CURLPROXY_SOCKS5);
  //  curl_setopt($z7, CURLOPT_PROXY, $proxy);
//curl_setopt($z7, CURLOPT_HTTPPROXYTUNNEL, $proxy);
 curl_setopt($z7, CURLOPT_SSL_VERIFYPEER, 0);
 curl_setopt($z7, CURLOPT_TIMEOUT, 10);
// curl_setopt($z7, CURLOPT_USERAGENT, $agent);
 curl_setopt($z7, CURLOPT_ENCODING, "gzip");
 $outp = curl_exec($z7);
 $data = curl_getinfo($z7);
 curl_close($z7);
 $d['code'] = $data['http_code'];
 $d['o'] = $outp;
 return $d;
}
$_ = view($url,$agent);
  if($_['code']==302){
    echo $_['code']." =>> redirect ke $urlredir \n";sleep(5);
}

function getskip($urlredir) {
//$url = 'http://advcrypt.com/ethterminalminer';
$ch = curl_init();
 curl_setopt($ch, CURLOPT_URL, $urlredir);
 curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'GET');
 curl_setopt($ch, CURLOPT_POST, 1);
//curl_setopt($ch, CURLOPT_POSTFIELDS, $body);
 curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
//$headers = array (
//'X-Unity-Version:2019.3.5f1'
  //      );
//curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
$result = curl_exec($ch);
return $result;}

echo "redir anda ".getskip($urlredir)."\n";
