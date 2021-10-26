// import statements  
import java.math.BigInteger;  
import java.security.NoSuchAlgorithmException;  
import java.security.MessageDigest;  
  
  
// A Java program that uses the MD5 to do the hashing  
public class MD5   
{  
public static String getMd5(String input)  
{  
try   
{  
  
// invoking the static getInstance() method of the MessageDigest class  
// Notice it has MD5 in its parameter.  
MessageDigest msgDst = MessageDigest.getInstance("MD5");  
  
// the digest() method is invoked to compute the message digest  
// from an input digest() and it returns an array of byte  
byte[] msgArr = msgDst.digest(input.getBytes());  
  
// getting signum representation from byte array msgArr  
BigInteger bi = new BigInteger(1, msgArr);  
  
// Converting into hex value  
String hshtxt = bi.toString(16);  
  
while (hshtxt.length() < 32)   
{  
hshtxt = "0" + hshtxt;  
}  
return hshtxt;  
}  
// for handling the exception   
catch (NoSuchAlgorithmException abc)   
{  
throw new RuntimeException(abc);  
}  
}  
// main method code  
public static void main(String argvs[]) throws NoSuchAlgorithmException  
{  
String str = "Sample";  
String hash = getMd5(str);  
str = "'Sample'";  
System.out.println("The HashCode Generated for " + str + " is: " + hash);  
}  
}
