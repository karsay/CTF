import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.security.InvalidAlgorithmParameterException;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;

import javax.crypto.BadPaddingException;
import javax.crypto.Cipher;
import javax.crypto.IllegalBlockSizeException;
import javax.crypto.NoSuchPaddingException;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;

public class Main {

    public static void main(String[] args) throws NoSuchAlgorithmException, IOException, NoSuchPaddingException, InvalidKeyException, InvalidAlgorithmParameterException, IllegalBlockSizeException, BadPaddingException {
        //jewel_c.pngの読み込み
        FileInputStream fs = new FileInputStream("jewel_c.png");
        byte abyte0[] = new byte[fs.available()];
        fs.read(abyte0);

        //jewel_c.pngの復号
        String s = "999999913371337";
        SecretKeySpec secretkeyspec = new SecretKeySpec((new StringBuilder("!")).append(s).toString().getBytes("ASCII"), "AES");
        IvParameterSpec ivparameterspec = new IvParameterSpec("kLwC29iMc4nRMuE5".getBytes());
        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
        cipher.init(2, secretkeyspec, ivparameterspec);
        byte abyte1[] = cipher.doFinal(abyte0);

        //復号したデータの書き込み
        FileOutputStream fileOutStm = new FileOutputStream("jewel.png");
        fileOutStm.write(abyte1);
    }
}