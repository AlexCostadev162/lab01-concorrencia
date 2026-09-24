import threading
import time

saldo_conta = 0
NUM_OPERACOES = 100000


def depositar():
    global saldo_conta

    for _ in range(NUM_OPERACOES):
        # Operação NÃO ATÔMICA:
        # leitura -> modificação -> escrita
        temp = saldo_conta

        # Facilita uma troca de contexto para tornar
        # a condição de corrida observável no experimento.
        time.sleep(0)

        temp = temp + 1
        saldo_conta = temp


def main():
    global saldo_conta

    print(f"[*] Saldo Inicial: {saldo_conta}")

    t1 = threading.Thread(target=depositar, name="Thread-Caixa-1")
    t2 = threading.Thread(target=depositar, name="Thread-App-2")

    inicio = time.time()

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    fim = time.time()

    saldo_esperado = NUM_OPERACOES * 2

    print(f"[*] Saldo Esperado: {saldo_esperado}")
    print(f"[!] Saldo Obtido:   {saldo_conta}")
    print(f"[*] Tempo: {fim - inicio:.6f} s")

    if saldo_conta != saldo_esperado:
        print("\n[ALERTA] Condição de Corrida detectada! Houve perda de dados.")
    else:
        print("\n[OK] Resultado íntegro.")


if __name__ == "__main__":
    main()
