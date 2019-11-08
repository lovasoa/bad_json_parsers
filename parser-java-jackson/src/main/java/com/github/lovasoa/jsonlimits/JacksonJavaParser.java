package com.github.lovasoa.jsonlimits;

import java.util.Objects;
import java.util.Scanner;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;

public class JacksonJavaParser {

    private static final Scanner SIN = new Scanner(System.in);

    public static void main(String[] args) throws JsonProcessingException {
        String fullInput = SIN.next();
        System.out.println("Full input: " + fullInput);
        JsonNode jsonTree = new ObjectMapper().readTree(fullInput);
        Objects.requireNonNull(jsonTree);
    }

}
