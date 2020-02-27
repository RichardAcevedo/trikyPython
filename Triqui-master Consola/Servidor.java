package logica;

import java.io.*;
import java.net.*;

public class Servidor{
    
    private static int PUERTO=2000;
    
    public static void main(String[] args) throws IOException{
        ServerSocket server=new ServerSocket(PUERTO);
        System.out.println("Esperando cliente...");
        Socket cliente=server.accept();
        
        String recibido="", enviado="";
        
        OutputStreamWriter salida = new OutputStreamWriter(cliente.getOutputStream(), "UTF8");
        InputStreamReader entrada = new InputStreamReader(cliente.getInputStream(), "UTF8");
        
        char[] bufer=new char[512];
        
        while(true){
            System.out.println("Esperando mensaje...");
            entrada.read(bufer);
            
            for (char c: bufer) {
                recibido+=c;
                if (c==0) {
                    break;
                }
            }
            
            System.out.println("Recibido: "+recibido);
            System.out.println("Enviar a cliente: "+recibido);
            recibido=""+recibido;
            
            salida.write(recibido.toCharArray());
            salida.flush();
            recibido="";
            
            bufer=new char[512];
        }
    }
}