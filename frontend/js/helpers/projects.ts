// Projects helper - vanilla JavaScript for simple enhancements
class ProjectsHelper {
  constructor() {
    this.init()
  }

  init() {
    console.log('📋 Projects helper initialized')
    this.setupProjectCards()
    this.setupFilters()
  }

  setupProjectCards() {
    const projectCards = document.querySelectorAll('[data-project-card]')
    
    projectCards.forEach(card => {
      // Add hover effects and click handlers
      card.addEventListener('mouseenter', this.onProjectHover.bind(this))
      card.addEventListener('click', this.onProjectClick.bind(this))
    })
  }

  setupFilters() {
    const filterButtons = document.querySelectorAll('[data-filter]')
    
    filterButtons.forEach(button => {
      button.addEventListener('click', (e) => {
        const filter = (e.target as HTMLElement).dataset.filter
        this.filterProjects(filter || 'all')
      })
    })
  }

  onProjectHover(event: Event) {
    const card = event.target as HTMLElement
    // Add some visual feedback
    console.log('Hovering over project:', card.dataset.projectId)
  }

  onProjectClick(event: Event) {
    const card = event.target as HTMLElement
    const projectId = card.dataset.projectId
    
    if (projectId) {
      // Navigate to project detail or open modal
      console.log('Clicked project:', projectId)
      // window.location.href = `/projects/${projectId}/`
    }
  }

  filterProjects(filter: string) {
    const projects = document.querySelectorAll('[data-project-card]')
    
    projects.forEach(project => {
      const projectStatus = (project as HTMLElement).dataset.status
      
      if (filter === 'all' || projectStatus === filter) {
        (project as HTMLElement).style.display = 'block'
      } else {
        (project as HTMLElement).style.display = 'none'
      }
    })
  }
}

// Initialize if we're on a projects page
if (document.querySelector('[data-page="projects"]')) {
  new ProjectsHelper()
}

export { ProjectsHelper }
