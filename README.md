# 5 Times's a Charm
Official write-up for a challenge in NasCon CTF '23

## Challenge
<b>Name</b><br/>
5 Times's a Charm<br/><br/>
<b>Description</b><br/>
A ransomware attack hit my machine and it turned one of my saved passwords into this. Please help me recover it. 
<br/><br/>
febad5d079bf253c0c76791687c47cfb<br/><br/>
<b>Hint</b><br/>
The attacker sent me a message saying "You rock!".

## Solve
#### Identifying the problem
The cipher-text given to us instantly lets us know it's a hash. By the looks of it, it looks like an MD5 digest. Let us confirm this by using ```hash-identifier```. Hash identifier confirms that the cipher text is most probably an MD5 digest.<br/>

![image](https://user-images.githubusercontent.com/88616338/226195225-ebb58c76-ad6e-4571-bf2a-a58d57a83e9a.png)

#### Cracking attempt 1
The first thing that probably anyone does after being given a hash, that needs to be cracked, is go to [CrackStation](https://crackstation.net/). <br/>
![image](https://user-images.githubusercontent.com/88616338/226195417-1b9c2902-5df3-4db6-848e-11c7e357c36c.png)
Unfortunately, CrackStation is not able to crack the hash :(

#### Cracking attempt 2
After being lost for a while and not knowing what to do, we are given a hint. We take up the hint (provided above), which hints us at the use of our most favorite wordlist ```rockyou.txt```. We go ahead and fire up <b>John the Ripper</b> to try and crack the hash using the rockyou wordlist.
```
echo "febad5d079bf253c0c76791687c47cfb" > hash
john hash --format=raw-md5 --wordlist=/usr/share/wordlists/rockyou.txt
```
Even John the Ripper fails us:<br/>
![image](https://user-images.githubusercontent.com/88616338/226195765-1a257541-d6be-454e-8f7b-e66383f70317.png)
Frustrated, we try and look at the problem statement again and we notice how the name is weird. Could the '5 Times' indicate anything other than 'MD5'? That leads to...

#### Cracking attempt 3
We get an amazing idea that maybe someone hashed a password 5 times as the name of the challenge is '5 Times's a Charm' and we write up a simple script (or ask ChatGPT to write it) to hash each password in a wordlist 5 times before comparing it with the target hash. [Here](crack.py) is a simple script that does exactly that. We fire up the script, providing it with the wordlist ```/usr/share/wordlists/rockyou.txt``` and viola!<br/>
![image](https://user-images.githubusercontent.com/88616338/226196254-da14c9f7-ea5d-4d7d-9ade-01ca44b10642.png)

## Conclusion 
The challenge is not always hard. Try to make the most out of the information given to you, including the name, description and hints.
