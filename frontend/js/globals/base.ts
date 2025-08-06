// Global base script - loaded on every page
// Note: CSS is now loaded separately via Vite entry points

// Global utilities and helpers
class GlobalApp {
  constructor() {
    // Apply dark mode immediately to prevent flash
    this.initializeTheme()
    this.init()
  }

  initializeTheme() {
    // Apply saved theme immediately before other initialization
    const savedTheme = localStorage.getItem('darkMode')
    if (savedTheme === 'true') {
      document.documentElement.classList.add('dark')
    } else if (savedTheme === 'false') {
      document.documentElement.classList.remove('dark')
    } else {
      // Auto-detect based on system preference
      if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
        document.documentElement.classList.add('dark')
      }
    }
  }

  init() {
    console.log('🌍 Global scripts initialized')
    this.setupDarkModeToggle()
    this.setupMobileMenu()
    this.setupGlobalEventListeners()
    
    // Reveal content after styles are loaded
    this.revealContent()
  }

  revealContent() {
    // Ensure content is visible after CSS loads
    document.documentElement.classList.add('ready')
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
