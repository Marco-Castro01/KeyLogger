package com.grupo1.keyloggerapi.repositories;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.grupo1.keyloggerapi.models.ExtractedDataModel;

@Repository
public interface ExtractedDataRepository extends CrudRepository<ExtractedDataModel, Long> {
    
    // Custom Services headers goes here

}
