package com.gitgalaxy.modernized.entity;

import lombok.Data;
import lombok.NoArgsConstructor;
import jakarta.persistence.*;
import java.math.BigDecimal;

@Data
@NoArgsConstructor
@Entity
@Table(name = "WS_REGISTRO")
public class WsRegistro {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "sys_id")
    private Long sysId;

    @Column(name = "WS_TEMA")
    private String wsTema;

    @Column(name = "WS_ID")
    private String wsId;

    @Column(name = "WS_NAME")
    private String wsName;

    @Column(name = "WS_SRCH")
    private String wsSrch;

    @Column(name = "WS_CODIGO")
    private String wsCodigo;

    @Column(name = "WS_NOMBRE")
    private String wsNombre;

}