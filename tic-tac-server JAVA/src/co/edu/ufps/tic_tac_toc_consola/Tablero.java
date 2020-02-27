/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package co.edu.ufps.tic_tac_toc_consola;

/**
 *
 * @author john
 */
public class Tablero {
    private char[][] posiciones;

    public Tablero() {
        this.posiciones = new char[3][3];
    }

    public void reiniciarTablero () {
        this.posiciones = new char[3][3];
    }

    public boolean tableroLleno () {
        for (char[] x: this.posiciones) {
            for (char y: x ) {
                if (y == 0) {
                    return false;
                }
            }
        }
        return true;
    }

    public int agregarMovimiento(int x, int y, char marca) {
        posiciones[y][x] = marca;
        
        if (this.validarVictoria(marca)) {
            return 1;
        }
        if (this.tableroLleno()) {
            return 0;
        }
        return -1;
    }

    public boolean esLibre(int x, int y) {
        if (posiciones[y][x] == 0) {
            return true;
        }
        return false;
    }

    private boolean validarVictoria (char marca) {
        return this.validarColumnas(0, marca) || this.validarFilas(0, marca)
                || this.validarDiagonales(marca);
    }

    public boolean validarColumnas (int numeroColumna, char marca) {
        if (numeroColumna == 3) {
            return false;
        }
        for (int i = 0; i<this.posiciones.length; i++) {
            if (posiciones[numeroColumna][i] == 0 ) {
                numeroColumna++;
                return validarColumnas(numeroColumna, marca);
            }
            if (posiciones[numeroColumna][i] != marca) {
                numeroColumna++;
                return validarColumnas(numeroColumna, marca);
            }
        }
        return true;
    }

    public boolean validarFilas (int numeroFila, char marca) {
        if (numeroFila == 3) {
            return false;
        }
        for (int i = 0; i<this.posiciones.length; i++) {
            if (posiciones[i][numeroFila] == 0 ) {
                numeroFila++;
                return validarFilas(numeroFila, marca);
            }
            if (posiciones[i][numeroFila] != marca) {
                numeroFila++;
                return validarFilas(numeroFila, marca);
            }
        }
        return true;
    }

    public boolean validarDiagonales (char marca) {
        for (int i = 0; i < this.posiciones.length; i++) {
            if (this.posiciones[i][i] != marca) {
                break;
            }
            if (this.posiciones[i][i] == marca && i == this.posiciones.length - 1) {
                return true;
            }
        }
        for (int i = 0; i < this.posiciones.length; i++) {
            if (this.posiciones[i][(this.posiciones.length - 1) - i] != marca) {
                break;
            }
            if (this.posiciones[i][(this.posiciones.length - 1) - i]
                    == marca && i == this.posiciones.length - 1) {
                return true;
            }
        }
        return false;
    }

    public String mostrarTablero () {
        return toString();
    }

    @Override
    public String toString() {
        String cadena = "   0   1   2\n";
        int i = 0;
        for (char[] x: this.posiciones) {
            cadena += i + " ";
            for (char y: x ) {
                if (y == 0) {
                    y = ' ';
                }
                cadena += "[" + y + "] ";
            }
            cadena += "\n";
            i++;
        }
        return cadena;
    }

    public String transformarTablero () {
        String cadena = "";
        boolean primerValor = true;
        for (char[] x: this.posiciones) {
            for (char y: x ) {
                if (!primerValor) {
                    cadena += ",";
                }
                if (y == 0) {
                    y = ' ';
                }
                cadena += y;
                primerValor = false;
            }
        }
        return cadena;
    }
}
