# Project Variables

variable "project_name" {
  description = "Name of the project"
  type        = string
  default     = "iotbuilding"
}

variable "resource_group_name" {
  description = "Name of the resource group"
  type        = string
  default     = "iot-building-rg"
}

variable "location" {
  description = "Azure region to deploy resources"
  type        = string
  default     = "East US"
}

variable "environment" {
  description = "Environment name"
  type        = string
  default     = "dev"
}

variable "aks_node_count" {
  description = "Number of AKS nodes"
  type        = number
  default     = 1
}

variable "aks_vm_size" {
  description = "VM size for AKS nodes"
  type        = string
  default     = "Standard_D2s_v7"
}