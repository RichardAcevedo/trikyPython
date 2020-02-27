/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package co.edu.ufps.tic_tac_toc_consola;

import java.util.Scanner;
import java.util.regex.Pattern;

/**
 *
 * @author john
 */
public class Partida {
    private Usuario usuario1;
    private Usuario usuario2;
    private Tablero tablero;
    private Usuario siguienteJugador;
    private Usuario jugadorGanador;
    private Scanner sc;

    public Partida() {
        this.tablero = new Tablero();
        sc = new Scanner(System.in);
    }

    public Usuario getUsuario1() {
        return usuario1;
    }

    public Usuario getUsuario2() {
        return usuario2;
    }

    public void setUsuario1(Usuario usuario1) {
        this.siguienteJugador = usuario1;
        this.usuario1 = usuario1;
    }

    public void setUsuario2(Usuario usuario2) {
        this.usuario2 = usuario2;
    }

    

    public void empezarPartida () {
        System.out.println("Cargando....");
        boolean terminarJuego = true;
        do {
            System.out.println("Esperando movimiento del jugador: "
                    + getSiguienteJugador().getNombre());
            if (esperandoMovimientoJugador()) {
                terminarJuego = !terminarJuego();
            }
            System.out.println("///////////////////////////////////"
                    + "Turno del Siguiente Jugador//////////"
                    + "/////////////////////////");
        } while (terminarJuego);
    }

    public boolean esperandoMovimientoJugador () {
        boolean columnaValida = true;
        String columna = "";
        String fila = "";
        int[] posicion = new int[2];
        this.tablero.mostrarTablero();
        while (columnaValida) {
            System.out.println("Ingrese el valor de la COLUMNA (0, 1, 2) "
                    + "la cual quiere marcar...");
            columna = sc.nextLine();
            if (Pattern.matches("(0|1|2)", columna)) {
                posicion[0] = Integer.parseInt(columna);
                columnaValida = false;
            } else {
                System.out.println("Valor INVALIDO, intentelo de nuevo...");
            }
        }
        boolean filaValida = true;
        while (filaValida) {
            System.out.println("Ingrese el valor de la FILA (0, 1, 2) "
                    + "la cual quiere marcar...");
            fila = sc.nextLine();
            if (Pattern.matches("(0|1|2)", fila)) {
                posicion[1] = Integer.parseInt(fila);
                filaValida = false;
            } else {
                System.out.println("Valor INVALIDO, intentelo de nuevo...");
            }
        }
        if (!this.tablero.esLibre(posicion[0], posicion[1])) {
            System.out.println("Esta posición no esta libre, intentelo de nuevo...");
            return esperandoMovimientoJugador();
        }
        return agregarMovimiento(posicion[0], posicion[1], siguienteJugador.getMarca());
    }

    public boolean agregarMovimiento (String movimiento, char marca) {
        String[] coordenada = movimiento.split(",");
        return this.agregarMovimiento(Integer.parseInt(coordenada[0]),
                Integer.parseInt(coordenada[1]), marca);
    }

    public boolean agregarMovimiento (int x, int y, char marca) {
        if (!this.tablero.esLibre(x, y)) {
            return false;
        }
        int resultadoPartida = this.tablero.agregarMovimiento(x, y, marca);
        if (resultadoPartida == 1) {
            tablero.mostrarTablero();
            System.out.println("El GANADOR de la partida es: "
                    + this.siguienteJugador.getNombre());
            this.siguienteJugador.setPuntaje(
                    this.siguienteJugador.getPuntaje() + 10);
            this.jugadorGanador = this.siguienteJugador;
            this.informarPerdedor();
        } else if (resultadoPartida == 0) {
            tablero.mostrarTablero();
            System.out.println("Hubo un EMPATE en la partida...");
            this.informarEmpate();
        }
        /*
            Se cambia el usuario al cual se le espera el siguiente movimiento
        */
        if (this.siguienteJugador == usuario1) {
            this.siguienteJugador = usuario2;
        } else {
            this.siguienteJugador = usuario1;
        }
        return true;
    }

    public boolean terminarJuego () {
        String respuesta = "";
        while (true) {
            System.out.println("Desea jugar de NUEVO?"
                    + "\nOprima 'S' para CONTINUAR o 'N' para SALIR");
            respuesta = sc.nextLine();
            if (respuesta.equalsIgnoreCase("N")) {
                return true;
            } else if (respuesta.equalsIgnoreCase("S")) {
                return false;
            }
        }
    }

    public String mostrarTablero () {
        return this.tablero.mostrarTablero();
    }

    public Usuario getSiguienteJugador() {
        return siguienteJugador;
    }

    public void setSiguienteJugador(Usuario siguienteJugador) {
        this.siguienteJugador = siguienteJugador;
    }

    public void removerUsuario (Usuario usuario) {
        if (this.usuario1 == usuario) {
            this.usuario1 = this.usuario2;
            this.usuario2 = null;
        } else if (this.usuario2 == usuario) {
            this.usuario2 = null;
        }
        this.siguienteJugador = this.usuario1;
    }

    public void reiniciarPartida () {
        this.jugadorGanador = null;
        this.tablero.reiniciarTablero();
    }

    public String tableroTransformado () {
        return this.tablero.transformarTablero();
    }

    public Usuario getJugadorGanador() {
        return jugadorGanador;
    }

    public void setJugadorGanador(Usuario jugadorGanador) {
        this.jugadorGanador = jugadorGanador;
    }

    public boolean tableroLleno() {
        return this.tablero.tableroLleno();
    }

    public void informarPerdedor () {
        if (this.usuario1 == this.jugadorGanador) {
            this.usuario2.setGanoPartida("-1");
        } else {
            this.usuario1.setGanoPartida("-1");
        }
    }

    public void informarEmpate () {
        if (this.usuario1 == this.siguienteJugador) {
            this.usuario2.setGanoPartida("0");
        } else {
            this.usuario1.setGanoPartida("0");
        }
    }
}
