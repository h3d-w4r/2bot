<?php
class proxy {
private $response;
private $proxy;

function ambilProxy() {
$url = 'https://free-proxy-list.net/';
$http = 'https://www.socks-proxy.net/';
$url1 = 'https://www.proxydocker.com/en/socks5-list/';
 	echo '#> Mengambil proxy...' . PHP_EOL;
		$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $http);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
$resp = curl_exec($ch);
curl_close($ch);
$this->response = $resp;
return $this;
        }

function satukan() {
preg_match_all('/<tr><td>([0-9.]+)<\/td><td>([0-9]+)<\/td>/', $this->response, $result);
        $this->proxy = array_combine($result[1], $result[2]);
                return $this;
        }

function checkProxy($timeout = 10) {
        $i = 0;
        foreach($this->proxy as $ip => $port) {
        echo "\e[44m#> Memeriksa proxy: ".$ip.':'.$port."\e[49m (".$i." of ".count($this->proxy).") | \e[4mCreated by 0xPanda\e[0m\r";
if($con = @fsockopen($ip, $port, $errno, $error, 10)) {
echo "\033[K#> \e[32mLive\e[0m => ".$ip.':'.$port.PHP_EOL;
file_put_contents('proxi.txt', $ip.':'.$port.PHP_EOL, FILE_APPEND);
                        } else {
echo "\033[K#> \e[31mDie\e[0m  => ".$ip.':'.$port .'|'.$error.PHP_EOL;
                        }
                        $i++;
                }
        }

}
$crawler = new Proxy();
$crawler->ambilProxy()->satukan()->checkProxy();
