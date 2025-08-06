import React, { useState, useEffect } from 'react'
import { createRoot } from 'react-dom/client'

interface Task {
  id: number
  title: string
  description: string
  status: string
  due_date?: string
}

const TasksApp: React.FC = () => {
  const [tasks, setTasks] = useState<Task[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    // Fetch tasks from Django API or use window data
    const fetchTasks = async () => {
      try {
        // You can pass initial data from Django template or fetch from API
        const initialData = (window as any).tasksData || []
        setTasks(initialData)
      } catch (error) {
        console.error('Failed to load tasks:', error)
      } finally {
        setLoading(false)
      }
    }

    fetchTasks()
  }, [])

  const updateTaskStatus = (taskId: number, newStatus: string) => {
    setTasks(prev => prev.map(task => 
      task.id === taskId ? { ...task, status: newStatus } : task
    ))
  }

  if (loading) {
    return (
      <div className="flex items-center justify-center p-8">
        <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-500"></div>
      </div>
    )
  }

  return (
    <div className="space-y-4">
      <div className="flex justify-between items-center">
        <h2 className="text-2xl font-bold text-gray-900 dark:text-white">
          Interactive Tasks ({tasks.length})
        </h2>
        <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
          Add Task
        </button>
      </div>
      
      <div className="grid gap-4">
        {tasks.map(task => (
          <div key={task.id} className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
            <div className="flex justify-between items-start">
              <div>
                <h3 className="text-lg font-semibold text-gray-900 dark:text-white">
                  {task.title}
                </h3>
                <p className="text-gray-600 dark:text-gray-300 mt-2">
                  {task.description}
                </p>
              </div>
              <select 
                value={task.status}
                onChange={(e) => updateTaskStatus(task.id, e.target.value)}
                className="ml-4 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 p-2 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white"
              >
                <option value="New">New</option>
                <option value="In Progress">In Progress</option>
                <option value="Completed">Completed</option>
              </select>
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}

// Initialize React app if container exists
const container = document.getElementById('tasks-react-app')
if (container) {
  const root = createRoot(container)
  root.render(<TasksApp />)
}

export default TasksApp
