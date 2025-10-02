import sys
import heapq
from collections import deque

class Task:
    """Representa una tarea con un ID, tiempo de inicio y duración."""

    def __init__(self, id, start_time, time_to_be_completed):
        self.id = id
        self.start_time = start_time
        self.time_to_be_completed = time_to_be_completed

    def set_start_time(self, start_time):
        """Establece el tiempo de inicio de la tarea."""
        self.start_time = start_time

    def get_end_time(self):
        """Calcula y retorna el tiempo de finalización de la tarea."""
        return self.start_time + self.time_to_be_completed


class Thread:
    """Representa un hilo de procesamiento que maneja tareas."""

    def __init__(self, id, task):
        self.id = id
        self.task = task
        self.last_time_for_completed_task = 0

    def __lt__(self, other):
        """
        Define la comparación para la cola de prioridad.
        La prioridad se basa en el tiempo de finalización de la tarea actual.
        Si los tiempos son iguales, el hilo con el ID más bajo tiene prioridad.
        """
        return self.task.get_end_time() < other.task.get_end_time() or \
               (self.task.get_end_time() == other.task.get_end_time() and self.id < other.id)

    def set_task(self, task):
        """Asigna una nueva tarea al hilo."""
        self.task = task

    def set_last_time_for_completed_task(self, last_time_for_completed_task):
        """Actualiza el tiempo en el que el hilo terminó su última tarea."""
        self.last_time_for_completed_task = last_time_for_completed_task


def parallel_processing(n: int, m: int, tasks_queue):
    """
    Simula la programación de tareas en hilos paralelos.

    Utiliza una cola de prioridad para asignar eficientemente las tareas
    al hilo que se liberará más pronto. Este es un enfoque codicioso (greedy)
    que garantiza una solución óptima.

    Args:
        n (int): El número de hilos.
        m (int): El número de tareas.
        tasks_queue (deque): Una cola de tareas a procesar.

    Returns:
        list: Una lista de tuplas (ID del hilo, tiempo de inicio) para cada tarea.
    """
    
    # Cola de prioridad que almacena los hilos.
    # El hilo con el menor tiempo de finalización estará siempre en la cima.
    priority_queue = []

    # Almacena los resultados: (id del hilo, tiempo de inicio de la tarea).
    initial_times_for_tasks = [None] * m

    # Inicialización: Los primeros 'n' hilos toman las primeras 'n' tareas.
    # El tiempo de inicio para estas tareas es 0.
    for i in range(n):
        if tasks_queue:
            task = tasks_queue.popleft()
            # La tarea tiene un start_time de 0 por defecto, así que no es necesario setearlo.
            heapq.heappush(priority_queue, Thread(i, task))
            initial_times_for_tasks[task.id] = (i, 0)
        else:
            # Si no hay suficientes tareas para todos los hilos, retornamos.
            return initial_times_for_tasks

    # Procesamiento del resto de las tareas.
    while tasks_queue:
        # 1. Obtenemos la siguiente tarea de la cola.
        task = tasks_queue.popleft()
        
        # 2. Obtenemos el hilo que se liberará más pronto (de la cola de prioridad).
        thread = heapq.heappop(priority_queue)
        
        # 3. El tiempo de inicio de la nueva tarea es el tiempo de finalización de la tarea anterior
        #    en este mismo hilo.
        thread.set_last_time_for_completed_task(thread.task.get_end_time())
        task.set_start_time(thread.last_time_for_completed_task)
        
        # 4. Asignamos la nueva tarea al hilo.
        thread.set_task(task)
        
        # 5. Insertamos el hilo de nuevo en la cola de prioridad,
        #    ahora con el nuevo tiempo de finalización.
        heapq.heappush(priority_queue, thread)
        
        # 6. Guardamos el resultado para esta tarea.
        initial_times_for_tasks[task.id] = (thread.id, thread.last_time_for_completed_task)

    return initial_times_for_tasks


def main():
    """Función principal para leer la entrada, procesar y mostrar la salida."""
    try:
        input_in = sys.stdin.readline()
        n, m = list(map(int, input_in.split()))
        tasks_times_to_be_completed_in = sys.stdin.readline()
        tasks_times_to_be_completed = list(map(int, tasks_times_to_be_completed_in.split()))
    except (IOError, ValueError):
        print("Entrada inválida. Asegúrate de proporcionar números enteros.")
        return

    tasks_queue = deque()
    for i, time_to_be_completed in enumerate(tasks_times_to_be_completed):
        tasks_queue.append(Task(i, 0, time_to_be_completed))

    times_for_tasks = parallel_processing(n, m, tasks_queue)
    for t in times_for_tasks:
        print(t[0], t[1])


if __name__ == "__main__":
    main()