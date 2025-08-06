// Global base script - loaded on every page
import "../../css/main.css"

// Global utilities and helpers
class GlobalApp {
  constructor() {
    this.init()
  }

  init() {
    console.log('🌍 Global scripts initialized')
    this.setupDarkModeToggle()
    this.setupMobileMenu()
    this.setupGlobalEventListeners()
  }

  setupDarkModeToggle() {
    // Add dark mode toggle functionality if needed
    const toggleButton = document.querySelector('[data-theme-toggle]')
    if (toggleButton) {
      toggleButton.addEventListener('click', this.toggleDarkMode.bind(this))
    }
  }

  setupMobileMenu() {
    // Mobile menu functionality
    const menuToggle = document.querySelector('[data-collapse-toggle="mobile-menu"]')
    const mobileMenu = document.getElementById('mobile-menu')
    
    if (menuToggle && mobileMenu) {
      menuToggle.addEventListener('click', () => {
        mobileMenu.classList.toggle('hidden')
      })
    }
  }

  setupGlobalEventListeners() {
    // Global form enhancements, CSRF tokens, etc.
    document.addEventListener('DOMContentLoaded', () => {
      console.log('📄 Page loaded, global enhancements active')
    })
  }

  toggleDarkMode() {
    document.documentElement.classList.toggle('dark')
    localStorage.setItem('darkMode', String(document.documentElement.classList.contains('dark')))
  }
}

// Initialize global app
new GlobalApp()

// Export for use by other scripts
export { GlobalApp }
