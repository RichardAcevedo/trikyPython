import tkinter
from tkinter import messagebox
import webbrowser
from ttt_client import TTTClientGame
import threading
import socket

C_WINDOW_WIDTH = 640;
C_WINDOW_HEIGHT = 480;
C_WINDOW_MIN_WIDTH = 480;
C_WINDOW_MIN_HEIGHT = 360;
C_COLOR_BLUE_LIGHT = "#fff";
C_COLOR_BLUE_DARK = "#000";
C_COLOR_BLUE = "#fff";
C_COLOR_RED = "#f00"

class CanvasWidget:

	__count = 0; 

	def __init__(self, canvas):
		self.canvas = canvas;
		self.id = str(CanvasWidget.__count);
		CanvasWidget.__count = CanvasWidget.__count + 1;
		self.tag_name = self.__class__.__name__ + self.id;
		self.__disabled__ = False;
		self.normal_color = C_COLOR_BLUE; 
		self.hovered_color = C_COLOR_BLUE_DARK;

	def set_clickable(self, clickable):
		if(clickable):
			self.canvas.tag_bind(self.tag_name, "<Button-1>", 
				self.__on_click__);
		else:
			self.canvas.tag_unbind(self.tag_name, "<Button-1>");

	def __on_click__(self, event):
		if(self.__disabled__):
			return False;
		if self.command is not None:
			self.command();
			return True;
		else:
			print("Error: " + self.__class__.__name__ + " " + 
				self.id + " does not have a command");
			raise AttributeError;
		return False;

	def set_hoverable(self, hoverable):
		if(hoverable):
			self.canvas.tag_bind(self.tag_name, "<Enter>", 
				self.__on_enter__);
			self.canvas.tag_bind(self.tag_name, "<Leave>", 
				self.__on_leave__);
		else:
			self.canvas.tag_unbind(self.tag_name, "<Enter>");
			self.canvas.tag_unbind(self.tag_name, "<Leave>");

	def __on_enter__(self, event):
		if(self.__disabled__):
			return False;
		self.canvas.itemconfig(self.tag_name, fill=self.hovered_color);
		return True;

	def __on_leave__(self, event):
		if(self.__disabled__):
			return False;
		self.canvas.itemconfig(self.tag_name, fill=self.normal_color);
		return True;

	def disable(self):
		self.__disabled__ = True;

	def enable(self):
		self.__disabled__ = False;

	def is_enabled(self):
		return self.__disabled__;

	def config(self, **kwargs):
		return self.canvas.itemconfig(self.tag_name, **kwargs);

	def delete(self):
		self.canvas.delete(self.tag_name);

class CanvasClickableLabel(CanvasWidget):
	def __init__(self, canvas, x, y, label_text, normal_color, 
		hovered_color):
		CanvasWidget.__init__(self, canvas);

		self.normal_color = normal_color;
		self.hovered_color = hovered_color;
		
		canvas.create_text(x, y, font="Helvetica 14 underline", 
			text=label_text, fill=self.normal_color, tags=(self.tag_name));
		
		self.set_hoverable(True);
		self.set_clickable(True);

class CanvasButton(CanvasWidget):
	WIDTH = 196;
	HEIGHT = 32;

	def __init__(self, canvas, x, y, button_text, normal_color, 
		hovered_color, normal_text_color, hovered_text_color):
		CanvasWidget.__init__(self, canvas);
		self.normal_color = normal_color;
		self.hovered_color = hovered_color;
		self.normal_text_color = normal_text_color;
		self.hovered_text_color = hovered_text_color;

		canvas.create_rectangle(x - self.WIDTH/2 + self.HEIGHT/2, 
			y - self.HEIGHT/2, x + self.WIDTH/2 - self.HEIGHT/2, 
			y + self.HEIGHT/2, fill=self.normal_color, outline="", 
			tags=(self.tag_name, "rect" + self.id));

		canvas.create_oval(x - self.WIDTH/2, y - self.HEIGHT/2, 
			x - self.WIDTH/2 + self.HEIGHT, y + self.HEIGHT/2, 
			fill=self.normal_color, outline="", 
			tags=(self.tag_name, "oval_l" + self.id));

		canvas.create_oval(x + self.WIDTH/2 - self.HEIGHT, 
			y - self.HEIGHT/2, x + self.WIDTH/2, y + self.HEIGHT/2,
			fill=self.normal_color, outline="", 
			tags=(self.tag_name, "oval_r" + self.id));

		canvas.create_text(x, y, font="Helvetica 16 bold", 
			text=button_text, fill=self.normal_text_color, 
			tags=(self.tag_name, "text" + self.id));

		self.set_hoverable(True);
		self.set_clickable(True);

	def __on_enter__(self, event):
		if(super().__on_enter__(event)):
			self.canvas.itemconfig("text" + self.id, 
				fill=self.hovered_text_color);

	def __on_leave__(self, event):
		if(super().__on_leave__(event)):
			self.canvas.itemconfig("text" + self.id, 
				fill=self.normal_text_color);

class CanvasSquare(CanvasWidget):

	def __init__(self, canvas, x, y, width, normal_color, hovered_color, 
		disabled_color):
		CanvasWidget.__init__(self, canvas);

		self.normal_color = normal_color;
		self.hovered_color = hovered_color;
		self.disabled_color = disabled_color;

		canvas.create_rectangle(x - width/2, y - width/2, x + width/2, 
			y + width/2, fill=self.normal_color, outline="", 
			tags=(self.tag_name, "oval" + self.id));

		self.set_hoverable(True);
		self.set_clickable(True);

	def disable(self):
		super().disable();
		self.canvas.itemconfig(self.tag_name, fill=self.disabled_color);

	def enable(self):
		super().enable();
		self.canvas.itemconfig(self.tag_name, fill=self.normal_color);

	def set_temp_color(self, color):
		self.canvas.itemconfig(self.tag_name, fill=color);

class BaseScene(tkinter.Canvas):
	def __init__(self, parent):
		tkinter.Canvas.__init__(self, parent, bg=C_COLOR_BLUE_LIGHT, 
			width=C_WINDOW_WIDTH, height=C_WINDOW_HEIGHT);

		self.bind("<Configure>", self.__on_resize__);
		self.width = C_WINDOW_WIDTH; 
		self.height = C_WINDOW_HEIGHT; 

	def __on_resize__(self, event):
		self.wscale = float(event.width)/self.width;
		self.hscale = float(event.height)/self.height;
		self.width = event.width;
		self.height = event.height;

		self.config(width=self.width, height=self.height);

		self.scale("all", 0, 0, self.wscale, self.hscale);

	def create_button(self, x, y, button_text, 
		normal_color=C_COLOR_BLUE, hovered_color=C_COLOR_BLUE_DARK, 
		normal_text_color=C_COLOR_BLUE_DARK, 
		hovered_text_color=C_COLOR_BLUE_LIGHT):
		return CanvasButton(self, x, y, button_text, 
			normal_color, hovered_color, 
			normal_text_color, hovered_text_color);

	def create_square(self, x, y, width,
		normal_color=C_COLOR_BLUE, hovered_color=C_COLOR_BLUE_DARK, 
		disabled_color=C_COLOR_BLUE_LIGHT):
		return CanvasSquare(self, x, y, width,
			normal_color, hovered_color, disabled_color);

	def create_clickable_label(self, x, y, button_text, 
		normal_color=C_COLOR_BLUE_DARK, hovered_color=C_COLOR_BLUE_LIGHT):

		return CanvasClickableLabel(self, x, y, button_text, 
			normal_color, hovered_color);

class WelcomeScene(BaseScene):

	def __init__(self, parent):

		super().__init__(parent);

		self.create_arc((-64, -368, C_WINDOW_WIDTH + 64, 192), 
			start=0, extent=-180, fill=C_COLOR_BLUE, outline="");

		try:
			self.logo_image = tkinter.PhotoImage(file="res/UFPS_Logo.png");
			logo = self.create_image((C_WINDOW_WIDTH/2, 
				C_WINDOW_HEIGHT/2 - 96), image=self.logo_image);
			self.title_image = tkinter.PhotoImage(file="res/Captura.png");
			title = self.create_image((C_WINDOW_WIDTH/2, 
				C_WINDOW_HEIGHT/2 + 48), image=self.title_image);
		except:	
			tkinter.messagebox.showerror("Error", "Can't create images.\n" +
				"Please make sure the res folder is in the same directory" + 
				" as this script.");

		play_btn = self.create_button(C_WINDOW_WIDTH/2, 
			C_WINDOW_HEIGHT/2 + 136, "Jugar");
		play_btn.command = self.__on_play_clicked__;
		self.addtag_all("all");

	def __on_play_clicked__(self):
		self.pack_forget();
		self.main_game_scene.pack();


class MainGameScene(BaseScene):

	def __init__(self, parent):
		super().__init__(parent);

		self.board_grids_power = 3; 
		self.board_width = 256; 

		self.create_arc((-128, C_WINDOW_HEIGHT - 64, C_WINDOW_WIDTH + 128, 
			C_WINDOW_HEIGHT + 368), start=0, extent=180, fill=C_COLOR_BLUE, 
			outline="");
		return_btn = self.create_button(C_WINDOW_WIDTH - 128, 32, "Atrás");
		return_btn.command = self.__on_return_clicked__;

		self.draw_board();

		player_self_text = self.create_text(96, 128, font="Helvetica 16", 
			fill=C_COLOR_BLUE_DARK, tags=("player_self_text"), anchor="n");
		player_match_text = self.create_text(C_WINDOW_WIDTH - 96, 128, 
			font="Helvetica 16", fill=C_COLOR_BLUE_DARK, 
			tags=("player_match_text"), anchor="n");

		notif_text = self.create_text(8, C_WINDOW_HEIGHT-8, anchor="sw",
			font="Helvetica 16", fill=C_COLOR_BLUE_DARK, tags=("notif_text"));

		self.restart_btn = None;

		self.addtag_all("all");

	def pack(self):
		super().pack();
		threading.Thread(target=self.__start_client__).start();

	def draw_board(self, board_line_width = 4):
		self.squares = [None] * self.board_grids_power ** 2;
		for i in range(0, self.board_grids_power):
			for j in range(0, self.board_grids_power):
				self.squares[i+j*3] = self.create_square(
					(C_WINDOW_WIDTH - self.board_width)/2 + 
					self.board_width/self.board_grids_power * i + 
					self.board_width / self.board_grids_power / 2,
					(C_WINDOW_HEIGHT - self.board_width)/2 + 
					self.board_width/self.board_grids_power * j + 
					self.board_width / self.board_grids_power / 2,
					self.board_width / self.board_grids_power);
				self.squares[i+j*3].disable();

		for i in range(1, self.board_grids_power):
			self.create_line((C_WINDOW_WIDTH - self.board_width)/2, 
				(C_WINDOW_HEIGHT - self.board_width)/2 + 
				self.board_width/self.board_grids_power * i, 
				(C_WINDOW_WIDTH + self.board_width)/2, 
				(C_WINDOW_HEIGHT - self.board_width)/2 + 
				self.board_width/self.board_grids_power * i, 
				fill=C_COLOR_BLUE_DARK, width=board_line_width);
			self.create_line((C_WINDOW_WIDTH - self.board_width)/2 + 
				self.board_width/self.board_grids_power * i, 
				(C_WINDOW_HEIGHT - self.board_width)/2, 
				(C_WINDOW_WIDTH - self.board_width)/2 + 
				self.board_width/self.board_grids_power * i, 
				(C_WINDOW_HEIGHT + self.board_width)/2, 
				fill=C_COLOR_BLUE_DARK, width=board_line_width);

	def __start_client__(self):
		self.client = TTTClientGameGUI();
		self.client.canvas = self;
		try:
			host = socket.gethostbyname('192.168.0.15');
		except:
			tkinter.messagebox.showerror("Error", "Failed to get the game "+ 
				"host address from the web domain.\n" + 
				"Plase check your connection.");
			self.__on_return_clicked__();
			return;
		if(self.client.connect(host, "8000")):
			self.client.start_game();
			self.client.close();

	def __on_return_clicked__(self):
		self.__clear_screen();
		self.client.client_socket = None;
		self.client = None;
		self.pack_forget();
		self.welcome_scene.pack();

	def set_notif_text(self, text):
		self.itemconfig("notif_text", text=text);

	def update_board_content(self, board_string):
		if(len(board_string) != self.board_grids_power ** 2):
			print("The board string should be " + 
				str(self.board_grids_power ** 2) + " characters long.");
			raise Exception;

		self.delete("board_content");

		p = 16;

		for i in range(0, self.board_grids_power):
			for j in range(0, self.board_grids_power):

				if(board_string[i+j*3] == "O"):
					self.create_oval(
						(C_WINDOW_WIDTH - self.board_width)/2 + 
						self.board_width/self.board_grids_power * i + p,
						(C_WINDOW_HEIGHT - self.board_width)/2 + 
						self.board_width/self.board_grids_power * j + p,
						(C_WINDOW_WIDTH - self.board_width)/2 + 
						self.board_width/self.board_grids_power * (i + 1) - p,
						(C_WINDOW_HEIGHT - self.board_width)/2 + 
						self.board_width/self.board_grids_power * (j + 1) - p,
						fill="", outline=C_COLOR_BLUE_DARK, width=4,
						tags="board_content");
				elif(board_string[i+j*3] == "X"):
					self.create_line(
						(C_WINDOW_WIDTH - self.board_width)/2 + 
						self.board_width/self.board_grids_power * i + p,
						(C_WINDOW_HEIGHT - self.board_width)/2 + 
						self.board_width/self.board_grids_power * j + p,
						(C_WINDOW_WIDTH - self.board_width)/2 + 
						self.board_width/self.board_grids_power * (i + 1) - p,
						(C_WINDOW_HEIGHT - self.board_width)/2 + 
						self.board_width/self.board_grids_power * (j + 1) - p,
						fill=C_COLOR_BLUE_DARK, width=4,
						tags="board_content");
					self.create_line(
						(C_WINDOW_WIDTH - self.board_width)/2 + 
						self.board_width/self.board_grids_power * (i + 1) - p,
						(C_WINDOW_HEIGHT - self.board_width)/2 + 
						self.board_width/self.board_grids_power * j + p,
						(C_WINDOW_WIDTH - self.board_width)/2 + 
						self.board_width/self.board_grids_power * i + p,
						(C_WINDOW_HEIGHT - self.board_width)/2 + 
						self.board_width/self.board_grids_power * (j + 1) - p,
						fill=C_COLOR_BLUE_DARK, width=4,
						tags="board_content");

	def draw_winning_path(self, winning_path):
		for i in range(0, self.board_grids_power ** 2):
			if str(i) in winning_path: 
				self.squares[i].set_temp_color("#f00");


	def show_restart(self):
		self.restart_btn = self.create_button(C_WINDOW_WIDTH/2, C_WINDOW_HEIGHT - 32, 
			"Reiniciar", C_COLOR_BLUE_DARK, C_COLOR_BLUE_LIGHT, C_COLOR_BLUE_LIGHT, 
			C_COLOR_BLUE_DARK);
		self.restart_btn.command = self.__on_restart_clicked__;

	def __clear_screen(self):
		for i in range(0, self.board_grids_power ** 2):
			self.squares[i].disable();
			self.squares[i].set_temp_color(C_COLOR_BLUE_LIGHT);
		self.update_board_content(" " * self.board_grids_power ** 2);
		self.itemconfig("player_self_text", text="");
		self.itemconfig("player_match_text", text="");
		if self.restart_btn is not None:
			self.restart_btn.delete();
			self.restart_btn = None;

	def __on_restart_clicked__(self):
		self.__clear_screen();
		threading.Thread(target=self.__start_client__).start();


class TTTClientGameGUI(TTTClientGame):
	def __game_started__(self):
		self.canvas.set_notif_text("Juego Iniciado. " + 
			"Tienes \"" + self.role + "\"");
		self.canvas.itemconfig("player_self_text", 
			text="Eres:\n\nJugador " + str(self.player_id) + 
			"\n\nRol: " + self.role);
		self.canvas.itemconfig("player_match_text", 
			text="Rival:\n\nJugador " + str(self.match_id) + 
			"\n\nRol: " + ("O" if self.role == "X" else "X") );

	def __update_board__(self, command, board_string):
		"""(Override) Updates the board."""
		# Print the command-line board for debugging purpose
		super().__update_board__(command, board_string);
		# Draw the GUI board
		self.canvas.update_board_content(board_string);
		if(command == "D"):
			# If the result is a draw
			self.canvas.set_notif_text("Empate.");
			# Show the restart button
			self.canvas.show_restart();
		elif(command == "W"):
			# If this player wins
			self.canvas.set_notif_text("Ganaste!");
			# Show the restart button
			self.canvas.show_restart();
		elif(command == "L"):
			# If this player loses
			self.canvas.set_notif_text("Perdiste!");
			# Show the restart button
			self.canvas.show_restart();

	def __player_move__(self, board_string):
		"""(Override) Lets the user to make a move and sends it back to the
		server."""

		# Set user making move to be true
		self.making_move = True;

		for i in range(0, self.canvas.board_grids_power ** 2):
			# Check the board content and see if it's empty
			if(board_string[i] == " "):
				# Enable those squares to make them clickable
				self.canvas.squares[i].enable();
				# Bind their commands
				self.canvas.squares[i].command = (lambda self=self, i=i: 
					self.__move_made__(i));

		while self.making_move:
			pass;
	def __move_made__(self, index):

		print("User chose " + str(index + 1));

		for i in range(0, self.canvas.board_grids_power ** 2):
			self.canvas.squares[i].disable();
			self.canvas.squares[i].command = None;

		self.s_send("i", str(index + 1));
		self.making_move = False;

	def __draw_winning_path__(self, winning_path):
		super().__draw_winning_path__(winning_path);
		self.canvas.draw_winning_path(winning_path);
		
def main():
	root = tkinter.Tk();
	root.title("Triki Traki");
	root.minsize(C_WINDOW_MIN_WIDTH, C_WINDOW_MIN_HEIGHT);
	root.geometry(str(C_WINDOW_WIDTH) + "x" + str(C_WINDOW_HEIGHT));

	try:
		root.iconbitmap("res/UFPS_Logo2.ico");
	except:	
		

	welcome_scene = WelcomeScene(root);
	main_game_scene = MainGameScene(root);
	welcome_scene.main_game_scene = main_game_scene; 
	main_game_scene.welcome_scene = welcome_scene;

	welcome_scene.pack();
	    
	root.mainloop();

if __name__ == "__main__":
	main();