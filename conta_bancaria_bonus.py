import threading
import time

saldo_conta = 0
NUM_OPERACOES = 100000
lock_bancario = threading.Lock()


def depositar():
    global saldo_conta

    for _ in range(NUM_OPERACOES):
        with lock_bancario:
            saldo_conta += 1


def sacar():
    global saldo_conta

    for _ in range(NUM_OPERACOES):
        with lock_bancario:
            saldo_conta -= 1


def main():
    global saldo_conta

    print(f"[*] Saldo Inicial: {saldo_conta}")

    t1 = threading.Thread(target=depositar, name="Thread-Deposito-1")
    t2 = threading.Thread(target=depositar, name="Thread-Deposito-2")
    t3 = threading.Thread(target=sacar, name="Thread-Saque-1")

    inicio = time.time()

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    fim = time.time()

    saldo_esperado = NUM_OPERACOES

    print(f"[*] Saldo Esperado: {saldo_esperado}")
    print(f"[*] Saldo Obtido:   {saldo_conta}")
    print(f"[*] Tempo de Execução: {fim - inicio:.6f} s")

    if saldo_conta == saldo_esperado:
        print("\n[OK] Saldo final correto.")
    else:
        print("\n[ERRO] Saldo final incorreto.")


if __name__ == "__main__":
    main()
