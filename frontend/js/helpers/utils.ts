// Shared utilities used across the application

export class ApiClient {
  static async request(url: string, options: RequestInit = {}) {
    const defaultOptions: RequestInit = {
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': this.getCSRFToken(),
      },
      ...options,
    }

    try {
      const response = await fetch(url, defaultOptions)
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`)
      }
      return await response.json()
    } catch (error) {
      console.error('API request failed:', error)
      throw error
    }
  }

  static getCSRFToken(): string {
    const token = document.querySelector('[name=csrfmiddlewaretoken]') as HTMLInputElement
    return token ? token.value : ''
  }
}

export class NotificationManager {
  static show(message: string, type: 'success' | 'error' | 'info' = 'info') {
    // Create a simple notification system
    const notification = document.createElement('div')
    notification.className = `fixed top-4 right-4 p-4 rounded-lg shadow-lg z-50 ${
      type === 'success' ? 'bg-green-500' :
      type === 'error' ? 'bg-red-500' :
      'bg-blue-500'
    } text-white`
    notification.textContent = message

    document.body.appendChild(notification)

    // Auto remove after 3 seconds
    setTimeout(() => {
      notification.remove()
    }, 3000)
  }
}

export class DateFormatter {
  static formatRelative(date: string | Date): string {
    const now = new Date()
    const target = new Date(date)
    const diffMs = now.getTime() - target.getTime()
    const diffDays = Math.floor(diffMs / (1000 * 60 * 60 * 24))

    if (diffDays === 0) return 'Today'
    if (diffDays === 1) return 'Yesterday'
    if (diffDays < 7) return `${diffDays} days ago`
    
    return target.toLocaleDateString()
  }
}

export class FormHelper {
  static setupForm(formSelector: string, onSubmit?: (data: FormData) => void) {
    const form = document.querySelector(formSelector) as HTMLFormElement
    if (!form) return

    form.addEventListener('submit', async (e) => {
      e.preventDefault()
      const formData = new FormData(form)
      
      if (onSubmit) {
        onSubmit(formData)
      } else {
        // Default form submission
        try {
          await ApiClient.request(form.action, {
            method: form.method,
            body: formData,
          })
          NotificationManager.show('Form submitted successfully!', 'success')
        } catch (error) {
          NotificationManager.show('Form submission failed', 'error')
        }
      }
    })
  }
}
