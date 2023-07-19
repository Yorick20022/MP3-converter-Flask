const options = {
  root: null,
  rootMargin: '0px',
  threshold: 0.5
}

export const SetupObserver = (el, cb) => {
  const observer = new IntersectionObserver((intersection, observer) => {
    if (intersection[0].isIntersecting) {
      if (cb) cb()
      observer.unobserve(el)
    }
  }, options)

  observer.observe(el)
}