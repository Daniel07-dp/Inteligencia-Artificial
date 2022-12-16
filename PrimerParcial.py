{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 117,
   "metadata": {},
   "outputs": [],
   "source": [
    "#variables\n",
    "Dos Lobos = True\n",
    "Dos Cabras = True\n",
    "Dos Lechugas = True\n",
    "vivo = True\n",
    "Estado = True\n",
    "posibles=[]\n",
    "indice = 0\n",
    "pierde = True\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 118,
   "metadata": {},
   "outputs": [],
   "source": [
    "# mover los objetos\n",
    "def cambia(objeto):\n",
    "    if(objeto):\n",
    "        return False\n",
    "    else:\n",
    "        return True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 119,
   "metadata": {},
   "outputs": [],
   "source": [
    "# mover de derecha a izqueirda\n",
    "def QueLado(objeto):\n",
    "    if(objeto):\n",
    "        return \"derecha\"\n",
    "    else:\n",
    "        return \"izquierda\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 120,<
   "metadata": {},
   "outputs": [],
   "source": [
    "#cambiando los objetos\n",
    "def QuienCambia (Letra, Cabra, Lechuga, Lobo, Estado):\n",
    "    if(Letra == 1):\n",
    "        Lechuga =cambia(Lechuga)\n",
    "        Estado = cambia(Estado)\n",
    "    elif(Letra == 2):\n",
    "        Cabra = cambia(Cabra)\n",
    "        Estado = cambia(Estado)\n",
    "    elif(Letra == 3):\n",
    "        Lobo = cambia(Lobos)\n",
    "        Estado = cambia(Estado)\n",
    "    elif(Letra == 0):\n",
    "        Estado = cambia(Estado)\n",
    "\n",
    "    return Lechuga, Cabra, Lobo, Estado"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 121,
   "metadata": {},
   "outputs": [],
   "source": [
    "#imprime el movimiento de los objetos\n",
    "def estad(Lechuga, Cabra, Lobo):\n",
    "    print (\"La lechuga esta en la \" + QuienCambia(Lechuga))\n",
    "    print (\"La Cabra esta en la \" + QuienCambia(Cabra))\n",
    "    print(\"El lobo esta en la \" +  QuienCambia(Lobo))\n",
    "    print (\"\\n\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 122,
   "metadata": {},
   "outputs": [],
   "source": [
    "#error\n",
    "def Secomen(Lechuga, Cabra, Lobo, Estado):\n",
    "\n",
    "    siguevivo= True\n",
    "    if((Dos Lechugas == Dos Cabra) & (Estado != (Dos Lechugas & Dos Cabras))):\n",
    "        sigue_vivo = False\n",
    "        print(\"La Cabra se comio la Lechuga\")\n",
    "    elif((Dos Lobo== Dos Cabras)& (Estado!= (Dos Lobos & Dos Cabras))):\n",
    "        sigue_vivo = False\n",
    "        print(\"Dos lobos se comieron a dos Cabra\")\n",
    "    return siguevivo"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 123,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "podras decifrar el acertijo\n"
     ]
    }
   ],
   "source": [
    "#mueve los objetos\n",
    "def mover(Estado, Lobo, Cabra, Lechuga):\n",
    "    a=[]\n",
    "    a.append(0)\n",
    "    print(\"Puede Cambiar de lado(Escriba a)\")\n",
    "    if (Estado == Lechuga):\n",
    "        print(\"Puede mover la Lechuga (escriba L)\")\n",
    "        a.eppend(1)\n",
    "    if(Estado == Cabra):\n",
    "        print(\"Puede mover la Cabra (Escriba c)\")\n",
    "        a.append(2)\n",
    "    if (Estado == Lobo):\n",
    "        print(\"Puede mover al Lobo (escriba L)\")\n",
    "        a.append(3)\n",
    "    print (\"\\n\\n\")\n",
    "    return a\n",
    "print(\"Problema resuelto\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 124,
   "metadata": {},
   "outputs": [],
  },
  {
   "cell_type": "code",
   "execution_count": 125,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
    }
    {
     "ename": "TypeError",
     "evalue": "QuienCambia() missing 4 required positional arguments: 'Cabra', 'Lechuga', 'Lobo', and 'Estado'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn [125], line 3\u001b[0m\n\u001b[0;32m      1\u001b[0m Instrucciones()\n\u001b[0;32m      2\u001b[0m \u001b[39mwhile\u001b[39;00m((Lechuga \u001b[39m|\u001b[39m Lobo \u001b[39m|\u001b[39m Cabra)):\n\u001b[1;32m----> 3\u001b[0m     estad(Lechuga, Cabra, Lobo)\n\u001b[0;32m      4\u001b[0m     posibles\u001b[39m=\u001b[39m mover(Estado, Lobo, Cabra, Lechuga)\n\u001b[0;32m      5\u001b[0m     \u001b[39m#Que va a hacer...\u001b[39;00m\n",
      "Cell \u001b[1;32mIn [121], line 3\u001b[0m, in \u001b[0;36mestad\u001b[1;34m(Lechuga, Cabra, Lobo)\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[39mdef\u001b[39;00m \u001b[39mestad\u001b[39m(Lechuga, Cabra, Lobo):\n\u001b[1;32m----> 3\u001b[0m     \u001b[39mprint\u001b[39m (\u001b[39m\"\u001b[39m\u001b[39mLa lechuga esta en la \u001b[39m\u001b[39m\"\u001b[39m \u001b[39m+\u001b[39m QuienCambia(Lechuga))\n\u001b[0;32m      4\u001b[0m     \u001b[39mprint\u001b[39m (\u001b[39m\"\u001b[39m\u001b[39mLa Cabra esta en la \u001b[39m\u001b[39m\"\u001b[39m \u001b[39m+\u001b[39m QuienCambia(Cabra))\n\u001b[0;32m      5\u001b[0m     \u001b[39mprint\u001b[39m(\u001b[39m\"\u001b[39m\u001b[39mEl lobo esta en la \u001b[39m\u001b[39m\"\u001b[39m \u001b[39m+\u001b[39m  QuienCambia(Lobo))\n",
      "\u001b[1;31mTypeError\u001b[0m: QuienCambia() missing 4 required positional arguments: 'Cabra', 'Lechuga', 'Lobo', and 'Estado'"
     ]
    }
   ],
   "source": [
    "Instrucciones()\n",
    "while((Lechuga | Lobo | Cabra)):\n",
    "    estad(Lechuga, Cabra, Lobo)\n",
    "    posibles= mover(Estado, Lobo, Cabra, Lechuga)\n",
    "    #Que va a hacer...\n",
    "    vivo= Secomen(Lechuga, Cabra, Lobo, Estado)\n",
    "    if (vivo):\n",
    "        eleccion = input(\"Que decea hacer?: \")\n",
    "        try:\n",
    "            #mira si el valor existe \n",
    "            indice = posibles.index(int(eleccion))\n",
    "            Lechuga, Cabra, Lobo, Estado = QuienCambia (int(eleccion), Lechuga, Cabra, Lobo, Estado)\n",
    "        except:\n",
    "            print (\"No puede realizar esta accion\")\n",
    "\n",
    "    else:\n",
    "        pierde = True\n",
    "        break\n",
    "if(pierde):\n",
    "    print (\"Problema resuelto\")\n",
    "else:\n",
    "    print (\"Perdio\")\n",
    "\n",
    "\n",
    "    \n",
    "\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.10.7 64-bit",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.7"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "c63d8c7d738c2960218a10995aedf0a7f67a49a231e71037adf0440953cdb45b"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}