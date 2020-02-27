/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package co.edu.ufps.tic_tac_toc_consola;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

/**
 *
 * @author john
 */
public class ServidorSocket {

    private final int puerto = 8090;
    private LinkedList<Socket> usuarios;
    private List<Usuario> listaUsuario;
    private OutputStreamWriter out;
    private InputStreamReader in;

    public ServidorSocket () {
        usuarios = new LinkedList<Socket>();
        listaUsuario = new ArrayList<Usuario>();
    }

    public void escuchar() {
        try {
            //Creamos el socket servidor
            ServerSocket servidor = new ServerSocket(puerto, 2);
            System.out.println("Esperando jugadores....");
            Partida partida = new Partida();
            while (true) {
                //Espera a que un jugador se conecte con exito
                Socket usuario = servidor.accept();
                if (partida.getUsuario2() != null) {
                    partida = new Partida();
                }
                in = new InputStreamReader(usuario.getInputStream(), "UTF8");
                out = new OutputStreamWriter(usuario.getOutputStream(), "UTF8");
                System.out.println("Se conecto un jugador");
                //Se agrega el socket a la lista
                usuarios.add(usuario);
                out.write("Ya te agregé\nPor favor ingrese su usuario: ".toCharArray());
                out.flush();
                new HiloJugador(usuario, usuarios, partida, listaUsuario, out, in);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    //Funcion main para correr el servidor
    public static void main(String[] args) {
        ServidorSocket servidor= new ServidorSocket();
        servidor.escuchar();
    }
}
