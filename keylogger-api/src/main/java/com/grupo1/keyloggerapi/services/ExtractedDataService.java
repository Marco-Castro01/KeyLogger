package com.grupo1.keyloggerapi.services;

import java.util.ArrayList;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.grupo1.keyloggerapi.models.ExtractedDataModel;
import com.grupo1.keyloggerapi.repositories.ExtractedDataRepository;

@Service
public class ExtractedDataService {
    @Autowired
    ExtractedDataRepository extractedDataRepository;
    
    public ArrayList<ExtractedDataModel> obtainData(){
        return (ArrayList<ExtractedDataModel>) extractedDataRepository.findAll();
    }

    public ExtractedDataModel saveData(ExtractedDataModel extractedDataModel){
        return extractedDataRepository.save(extractedDataModel);
    }

    public Optional<ExtractedDataModel> obtainDataById(Long id){
        return extractedDataRepository.findById(id);
    }
    
    public boolean deleteDataById(Long id) {
        try{
            extractedDataRepository.deleteById(id);
            return true;                
        }catch(Exception err){
            return false;
        }
    }
}
