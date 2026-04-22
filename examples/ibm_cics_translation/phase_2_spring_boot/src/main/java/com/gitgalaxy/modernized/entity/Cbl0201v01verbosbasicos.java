package com.gitgalaxy.modernized.entity;

import lombok.Data;
import lombok.NoArgsConstructor;
import jakarta.persistence.*;
import java.math.BigDecimal;

@Data
@NoArgsConstructor
@Entity
@Table(name = "CBL0201V01VERBOSBASICOS")
public class Cbl0201v01verbosbasicos {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "sys_id")
    private Long sysId;

    @Column(name = "WS_NAME_CANAL")
    private String wsNameCanal;

    @Column(name = "WS_FECHA_SISTEMA")
    private String wsFechaSistema;

}