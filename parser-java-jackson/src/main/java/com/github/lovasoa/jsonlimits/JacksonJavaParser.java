package com.github.lovasoa.jsonlimits;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Objects;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;

public class JacksonJavaParser {

    private static final ObjectMapper OBJECT_MAPPER = new ObjectMapper();

    public static void main(String[] args) throws IOException {
        JsonNode jsonTree = OBJECT_MAPPER.readTree(new BufferedReader(new InputStreamReader(System.in)));
        Objects.requireNonNull(jsonTree);
    }

}
