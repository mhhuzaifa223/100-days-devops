package main

deny contains msg if {
  input.kind == "Pod"
  some container in input.spec.containers
  container.securityContext.privileged == true
  msg := "Privileged containers are not allowed"
}

deny contains msg if {
  input.kind == "Pod"
  some container in input.spec.containers
  endswith(container.image, ":latest")
  msg := "Images must not use the latest tag"
}
