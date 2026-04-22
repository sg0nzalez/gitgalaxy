package com.gitgalaxy.modernized.entity;

import lombok.Data;
import lombok.NoArgsConstructor;
import jakarta.persistence.*;
import java.math.BigDecimal;

@Data
@NoArgsConstructor
@Entity
@Table(name = "CBL0202V01INICIARLIZARVERBO")
public class Cbl0202v01iniciarlizarverbo {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "sys_id")
    private Long sysId;

    @Column(name = "WS_NOMBRE")
    private String wsNombre;

    @Column(name = "WS_ID")
    private Integer wsId;

    @Column(name = "WS_DIRECCION")
    private String wsDireccion;

    @Column(name = "WS_NUMERO")
    private String wsNumero;

    @Column(name = "WS_CIUDAD")
    private String wsCiudad;

    @Column(name = "WS_POSTAL")
    private String wsPostal;

}