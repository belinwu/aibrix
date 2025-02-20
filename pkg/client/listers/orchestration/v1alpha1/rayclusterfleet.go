/*
Copyright 2024 The Aibrix Team.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/
// Code generated by lister-gen. DO NOT EDIT.

package v1alpha1

import (
	v1alpha1 "github.com/vllm-project/aibrix/api/orchestration/v1alpha1"
	"k8s.io/apimachinery/pkg/api/errors"
	"k8s.io/apimachinery/pkg/labels"
	"k8s.io/client-go/listers"
	"k8s.io/client-go/tools/cache"
)

// RayClusterFleetLister helps list RayClusterFleets.
// All objects returned here must be treated as read-only.
type RayClusterFleetLister interface {
	// List lists all RayClusterFleets in the indexer.
	// Objects returned here must be treated as read-only.
	List(selector labels.Selector) (ret []*v1alpha1.RayClusterFleet, err error)
	// RayClusterFleets returns an object that can list and get RayClusterFleets.
	RayClusterFleets(namespace string) RayClusterFleetNamespaceLister
	RayClusterFleetListerExpansion
}

// rayClusterFleetLister implements the RayClusterFleetLister interface.
type rayClusterFleetLister struct {
	listers.ResourceIndexer[*v1alpha1.RayClusterFleet]
}

// NewRayClusterFleetLister returns a new RayClusterFleetLister.
func NewRayClusterFleetLister(indexer cache.Indexer) RayClusterFleetLister {
	return &rayClusterFleetLister{listers.New[*v1alpha1.RayClusterFleet](indexer, v1alpha1.Resource("rayclusterfleet"))}
}

// RayClusterFleets returns an object that can list and get RayClusterFleets.
func (s *rayClusterFleetLister) RayClusterFleets(namespace string) RayClusterFleetNamespaceLister {
	return rayClusterFleetNamespaceLister{listers.NewNamespaced[*v1alpha1.RayClusterFleet](s.ResourceIndexer, namespace)}
}

// RayClusterFleetNamespaceLister helps list and get RayClusterFleets.
// All objects returned here must be treated as read-only.
type RayClusterFleetNamespaceLister interface {
	// List lists all RayClusterFleets in the indexer for a given namespace.
	// Objects returned here must be treated as read-only.
	List(selector labels.Selector) (ret []*v1alpha1.RayClusterFleet, err error)
	// Get retrieves the RayClusterFleet from the indexer for a given namespace and name.
	// Objects returned here must be treated as read-only.
	Get(name string) (*v1alpha1.RayClusterFleet, error)
	RayClusterFleetNamespaceListerExpansion
}

// rayClusterFleetNamespaceLister implements the RayClusterFleetNamespaceLister
// interface.
type rayClusterFleetNamespaceLister struct {
	listers.ResourceIndexer[*v1alpha1.RayClusterFleet]
}
