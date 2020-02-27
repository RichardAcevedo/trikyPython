/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package co.edu.ufps.tic_tac_toc_consola;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;

/**
 *
 * @author john
 */
public class Usuario {
    private String nombre;
    private int puntaje;
    private String victorias;
    private char marca;
    private Socket cliente;
    private DataOutputStream out;
    private DataInputStream in;
    private String ganoPartida;
    private boolean jugando;
    //El puerto debe ser el mismo en el que escucha el servidor
    private int puerto = 8090;
    //Si estamos en nuestra misma maquina usamos localhost si no la ip de la maquina servidor
    private String host = "localhost";

    public Usuario (String nombreDefecto) throws IOException {
        this.nombre = nombreDefecto;
        this.puntaje = 0;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        if (nombre == null || nombre.equals("")) {
            return;
        }
        this.nombre = nombre;
    }

    public int getPuntaje() {
        return puntaje;
    }

    public void setPuntaje(int puntaje) {
        this.puntaje = puntaje;
    }

    public String getVictorias() {
        return victorias;
    }

    public void setVictorias(String victorias) {
        this.victorias = victorias;
    }

    public char getMarca() {
        return marca;
    }

    public void setMarca(char marca) {
        this.marca = marca;
    }

    public String getGanoPartida() {
        return ganoPartida;
    }

    public void setGanoPartida(String ganoPartida) {
        this.ganoPartida = ganoPartida;
    }

    public boolean isJugando() {
        return jugando;
    }

    public void setJugando(boolean jugando) {
        this.jugando = jugando;
    }

}
